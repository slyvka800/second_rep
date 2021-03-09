import classes.package_of_disposable_tableware as father


class Cutlery(father.PackageOfDisposableTableware):
    def __init__(self, amount_of_pieces, origin_country: father.Country, type_of_dishes: father.Dishes,
                 material: father.Material, price, brand, thickness: father.Thickness, date_of_manufacture: list,
                 length_in_inches):
        super().__init__(amount_of_pieces, origin_country, type_of_dishes, material, price, brand, thickness,
                         date_of_manufacture)
        self._length_in_inches = length_in_inches
        self._output = ''

    def __str__(self):
        self._output = super().__str__() + f'\nlength in inches: {self._length_in_inches}'
        return self._output
