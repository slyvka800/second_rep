import classes.plates_and_bowls as plates_and_bowls


class Plate(plates_and_bowls.PlatesAndBowls):
    def __init__(self, amount_of_pieces, origin_country: plates_and_bowls.package.Country,
                 type_of_dishes: plates_and_bowls.package.Dishes, material: plates_and_bowls.package.Material,
                 price, brand, thickness: plates_and_bowls.package.Thickness, date_of_manufacture: list, diameter_in_cm,
                 deepness_in_cm, color, decoration):
        super().__init__(amount_of_pieces, origin_country, type_of_dishes, material, price, brand,
                         thickness, date_of_manufacture, diameter_in_cm, deepness_in_cm)
        self._color = color
        self._decoration = decoration
        self._output = ''

    def __str__(self):
        self._output = f'It is a plate\n' + super().__str__() + f'color: {self._color}\n'\
                         + f'decoration: {self._decoration}\n'
        return self._output
