import classes.package_of_disposable_tableware as father


class Drinkware(father.PackageOfDisposableTableware):
    def __init__(self, amount_of_pieces, origin_country: father.Country, type_of_dishes: father.Dishes,
                 material: father.Material, price, brand, thickness: father.Thickness, date_of_manufacture: list,
                 volume_in_litres, transparency_in_per_cents):
        super().__init__(amount_of_pieces, origin_country, type_of_dishes, material, price, brand, thickness,
                         date_of_manufacture)
        self._volume_in_litres = volume_in_litres
        self._transparency_in_per_cents = transparency_in_per_cents
        self._output = ''

    def __str__(self):
        self._output = super().__str__() + f'\nvolume in litres: {self._volume_in_litres}\n' \
                        + f'transparency in per cents: {self._transparency_in_per_cents}\n'
        return self._output
