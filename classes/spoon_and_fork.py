import classes.cutlery as cutlery
from enum import Enum


class SpoonType(Enum):
    TableSpoon = 1
    TeaSpoon = 2


class Spoon(cutlery.Cutlery):
    def __init__(self, amount_of_pieces, origin_country: cutlery.father.Country, type_of_dishes: cutlery.father.Dishes,
                 material: cutlery.father.Material, price, brand, thickness: cutlery.father.Thickness,
                 date_of_manufacture: list, length_in_inches, spoon_type: SpoonType):
        super().__init__(amount_of_pieces, origin_country, type_of_dishes, material, price, brand, thickness,
                         date_of_manufacture, length_in_inches)
        self._spoon_type = spoon_type
        self._output = ''

    def __str__(self):
        self._output = 'It is a spoon\n' + super(Spoon, self).__str__() + '\n'
        self._output += f'spoon type: {self._spoon_type.name}\n'
        return self._output


class Fork(cutlery.Cutlery):
    def __init__(self, amount_of_pieces, origin_country: cutlery.father.Country, type_of_dishes: cutlery.father.Dishes,
                 material: cutlery.father.Material, price, brand, thickness: cutlery.father.Thickness,
                 date_of_manufacture: list, length_in_inches, prong_amount):
        super().__init__(amount_of_pieces, origin_country, type_of_dishes, material, price, brand, thickness,
                         date_of_manufacture, length_in_inches)
        self._prong_amount = prong_amount
        self._output = ''

    def __str__(self):
        self._output = 'It is a fork\n' + super(Fork, self).__str__() + '\n'
        self._output += f'prong amount: {self._prong_amount}\n'
        return self._output


#a = Spoon(12, cutlery.father.Country.Ukraine, cutlery.father.Dishes.Spoons, cutlery.father.Material.Paper, 123,
#          "Nice Tableware", cutlery.father.Thickness.Low, [12, 28, 2002], 1240, SpoonType.TableSpoon)
#print(Spoon.__mro__)
#print(a.__str__())