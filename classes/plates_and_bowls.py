import classes.package_of_disposable_tableware as package


class PlatesAndBowls(package.PackageOfDisposableTableware):
    def __init__(self, amount_of_pieces, origin_country: package.Country, type_of_dishes: package.Dishes,
                 material: package.Material, price, brand, thickness: package.Thickness, date_of_manufacture: list,
                 diameter_in_cm, deepness_in_cm):
        super().__init__(amount_of_pieces, origin_country, type_of_dishes, material, price, brand, thickness,
                         date_of_manufacture)
        self._diameter_in_cm = diameter_in_cm
        self._deepness_in_cm = deepness_in_cm
        self._output = ''

    def __str__(self):
        self._output = super().__str__() + f'\ndiameter in cm: {self._diameter_in_cm}\n' \
                        + f'deepness in cm {self._deepness_in_cm}\n'
        return self._output



a = PlatesAndBowls(20, package.Country.Ukraine, package.Dishes.Plates,
                   package.Material.Wood, 45, 'DODO', package.Thickness.High, [12, 23, 45], 34, 45)
#print(a.__dict__)
