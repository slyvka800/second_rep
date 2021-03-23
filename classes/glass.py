import classes.drinkware as drinkware


class Glass(drinkware.Drinkware):
    def __init__(self, amount_of_pieces, origin_country: drinkware.father.Country,
                 type_of_dishes: drinkware.father.Dishes, material: drinkware.father.Material, price, brand,
                 thickness: drinkware.father.Thickness, date_of_manufacture: list, volume_in_litres,
                 transparency_in_per_cents, color, decorations):
        super().__init__(amount_of_pieces, origin_country, type_of_dishes, material, price, brand, thickness,
                         date_of_manufacture, volume_in_litres, transparency_in_per_cents)
        self._color = color
        self._decorations = decorations
        self._output = ''

    def __str__(self):
        self._output = 'It is a glass\n' + super().__str__() + f'color: {self._color}\n' \
                        + f'decoration: {self._decorations}\n'
        return self._output
