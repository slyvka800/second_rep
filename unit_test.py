import unittest
from manager.tableware_manager import *
from classes.cutlery import *
from classes.plates_and_bowls import *
from classes.package_of_disposable_tableware import *
from classes.drinkware import *
from classes.spoon_and_fork import *
from classes.plate import *
from classes.glass import *


class TestTablewareManager(unittest.TestCase):

    def test_sort_selection_by_price(self):
        input_list_asc = [Glass(10, Country.Ukraine, Dishes.Glass, Material.Wood, 35, "Coca-Cola", Thickness.Low,
                                [23, 12, 2019], 0.5, 35, 'blue', 'stripes'),
                          Spoon(20, Country.China, Dishes.Spoons, Material.Wood, 100, "Nice Company",
                                Thickness.High, [30, 12, 2021], 34, SpoonType.TableSpoon),
                          Fork(70, Country.Ukraine, Dishes.Forks, Material.Wood, 90, "Hot and Dog",
                               Thickness.Medium, [15, 8, 2016], 6, 5)]
        output_list_asc = [Glass(10, Country.Ukraine, Dishes.Glass, Material.Wood, 35, "Coca-Cola", Thickness.Low,
                                 [23, 12, 2019], 0.5, 35, 'blue', 'stripes'),
                           Fork(70, Country.Ukraine, Dishes.Forks, Material.Wood, 90, "Hot and Dog",
                                Thickness.Medium, [15, 8, 2016], 6, 5),
                           Spoon(20, Country.China, Dishes.Spoons, Material.Wood, 100, "Nice Company",
                                 Thickness.High, [30, 12, 2021], 34, SpoonType.TableSpoon)]
        manager = TablewareManager(*input_list_asc)
        input_list_desc = output_list_asc[:]
        output_list_desc = output_list_asc[::-1]

        input_list_asc = manager.sort_selection_by_price(input_list_asc)
        for i in range(len(input_list_asc)):
            input_list_asc[i] = input_list_asc[i].__str__()
            output_list_asc[i] = output_list_asc[i].__str__()
        self.assertEqual(input_list_asc, output_list_asc)

        input_list_desc = manager.sort_selection_by_price(input_list_desc, SortOrder.DESC)
        for i in range(len(input_list_desc)):
            input_list_desc[i] = input_list_desc[i].__str__()
            output_list_desc[i] = output_list_desc[i].__str__()
        self.assertEqual(input_list_desc, output_list_desc)

    def test_sort_selection_by_manufacture_date(self):
        input_list = [Glass(10, Country.Ukraine, Dishes.Glass, Material.Wood, 35, "Coca-Cola", Thickness.Low,
                            [23, 12, 2019], 0.5, 35, 'blue', 'stripes'),
                      Spoon(20, Country.China, Dishes.Spoons, Material.Wood, 100, "Nice Company",
                            Thickness.High, [30, 12, 2021], 34, SpoonType.TableSpoon),
                      Fork(70, Country.Ukraine, Dishes.Forks, Material.Wood, 90, "Hot and Dog",
                           Thickness.Medium, [15, 8, 2016], 6, 5)]
        output_list = [Fork(70, Country.Ukraine, Dishes.Forks, Material.Wood, 90, "Hot and Dog",
                            Thickness.Medium, [15, 8, 2016], 6, 5),
                       Glass(10, Country.Ukraine, Dishes.Glass, Material.Wood, 35, "Coca-Cola", Thickness.Low,
                             [23, 12, 2019], 0.5, 35, 'blue', 'stripes'),
                       Spoon(20, Country.China, Dishes.Spoons, Material.Wood, 100, "Nice Company",
                             Thickness.High, [30, 12, 2021], 34, SpoonType.TableSpoon)]
        manager = TablewareManager(*input_list)
        input_list = manager.sort_selection_by_manufacture_date(selected_packages=input_list)
        for i in range(len(input_list)):
            input_list[i] = input_list[i].__str__()
            output_list[i] = output_list[i].__str__()
        self.assertEqual(input_list, output_list)

    def test_search_by_material(self):
        manager = TablewareManager(
            Glass(10, Country.Ukraine, Dishes.Glass, Material.Wood, 35, "Coca-Cola", Thickness.Low,
                  [23, 12, 2019], 0.5, 35, 'blue', 'stripes'),
            Spoon(20, Country.China, Dishes.Spoons, Material.Wood, 100, "Nice Company",
                  Thickness.High, [30, 12, 2021], 34, SpoonType.TableSpoon),
            Fork(30, Country.Turkey, Dishes.Forks, Material.Plastic, 12, "Pepsi", Thickness.Low,
                 [6, 5, 2020], 34, 3),
            Plate(40, Country.China, Dishes.Plates, Material.Paper, 130, "Cool company", Thickness.High,
                  [6, 5, 2030], 12, 34, 'red', 'dots'),
            Glass(50, Country.Turkey, Dishes.Glass, Material.Plastic, 35, "Good glass",
                  Thickness.Medium, [3, 11, 2015], 1, 25, 'green', 'flowers'),
            Spoon(60, Country.China, Dishes.Spoons, Material.Paper, 115, "Coca-Cola",
                  Thickness.High, [31, 6, 2018], 45, SpoonType.TeaSpoon),
            Fork(70, Country.Ukraine, Dishes.Forks, Material.Wood, 90, "Hot and Dog",
                 Thickness.Medium, [15, 8, 2016], 6, 5),
            Plate(80, Country.Turkey, Dishes.Plates, Material.Plastic, 130, "Jeremy`s co.",
                  Thickness.Low, [28, 12, 2002], 68, 2.5, 'pink', 'hearts'))
        founds = manager.search_by_material(Material.Paper)
        founds = [i.__str__() for i in founds]
        correct_founds = [
            Plate(40, Country.China, Dishes.Plates, Material.Paper, 130, "Cool company", Thickness.High,
                  [6, 5, 2030], 12, 34, 'red', 'dots').__str__(),
            Spoon(60, Country.China, Dishes.Spoons, Material.Paper, 115, "Coca-Cola",
                  Thickness.High, [31, 6, 2018], 45, SpoonType.TeaSpoon).__str__()
        ]
        self.assertEqual(founds, correct_founds)


class TestCutlery(unittest.TestCase):
    def test__init__(self):
        cutlery_obj = Cutlery(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija", Thickness.Low,
                              [23, 3, 2021], 3.1)
        assert cutlery_obj._amount_of_pieces == 13
        assert cutlery_obj._origin_country == Country.Ukraine
        assert cutlery_obj._type_of_dishes == Dishes.Spoons
        assert cutlery_obj._material == Material.Paper
        assert cutlery_obj._price == 45
        assert cutlery_obj._brand == "Premija"
        assert cutlery_obj._thickness == Thickness.Low
        assert cutlery_obj._date_of_manufacture == [23, 3, 2021]
        assert cutlery_obj._length_in_inches == 3.1

    def test__str__(self):
        cutlery_obj = Cutlery(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija", Thickness.Low,
                              [23, 3, 2021], 3.1)
        cutlery_obj_str = cutlery_obj.__str__()
        correct_output = f'amount of pieces: 13 \n' \
                         f'origin country: Ukraine \n' \
                         f'type of dishes: Spoons \n' \
                         f'material: Paper \n' \
                         f'price: 45 \n' \
                         f'brand: Premija \n' \
                         f'thickness: Low \n' \
                         f'date of manufacture: [23, 3, 2021]' \
                         f'\nlength in inches: 3.1'
        self.assertEqual(cutlery_obj_str, correct_output)


class TestPlatesAndBowls(unittest.TestCase):
    def test__init__(self):
        plates_and_bowls_obj = PlatesAndBowls(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija",
                                              Thickness.Low, [23, 3, 2021], 6, 12)
        assert plates_and_bowls_obj._amount_of_pieces == 13
        assert plates_and_bowls_obj._origin_country == Country.Ukraine
        assert plates_and_bowls_obj._type_of_dishes == Dishes.Spoons
        assert plates_and_bowls_obj._material == Material.Paper
        assert plates_and_bowls_obj._price == 45
        assert plates_and_bowls_obj._brand == "Premija"
        assert plates_and_bowls_obj._thickness == Thickness.Low
        assert plates_and_bowls_obj._date_of_manufacture == [23, 3, 2021]
        assert plates_and_bowls_obj._diameter_in_cm == 6
        assert plates_and_bowls_obj._deepness_in_cm == 12

    def test__str__(self):
        plates_and_bowls_obj = PlatesAndBowls(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija",
                                              Thickness.Low,
                                              [23, 3, 2021], 6, 12)
        plates_and_bowls_obj_str = plates_and_bowls_obj.__str__()
        correct_output = f'amount of pieces: 13 \n' \
                         f'origin country: Ukraine \n' \
                         f'type of dishes: Spoons \n' \
                         f'material: Paper \n' \
                         f'price: 45 \n' \
                         f'brand: Premija \n' \
                         f'thickness: Low \n' \
                         f'date of manufacture: [23, 3, 2021]' \
                         f'\ndiameter in cm: 6\n' \
                         f'deepness in cm 12\n'
        self.assertEqual(plates_and_bowls_obj_str, correct_output)


class TestPackageOfDisposableTableware(unittest.TestCase):
    def test__init__(self):
        package_of_disposable_tableware_obj = PackageOfDisposableTableware(13, Country.Ukraine, Dishes.Spoons,
                                                                           Material.Paper, 45, "Premija", Thickness.Low,
                                                                           [23, 3, 2021])
        assert package_of_disposable_tableware_obj._amount_of_pieces == 13
        assert package_of_disposable_tableware_obj._origin_country == Country.Ukraine
        assert package_of_disposable_tableware_obj._type_of_dishes == Dishes.Spoons
        assert package_of_disposable_tableware_obj._material == Material.Paper
        assert package_of_disposable_tableware_obj._price == 45
        assert package_of_disposable_tableware_obj._brand == "Premija"
        assert package_of_disposable_tableware_obj._thickness == Thickness.Low
        assert package_of_disposable_tableware_obj._date_of_manufacture == [23, 3, 2021]

    def test__str__(self):
        package_of_disposable_tableware_obj = PackageOfDisposableTableware(13, Country.Ukraine, Dishes.Spoons,
                                                                           Material.Paper, 45, "Premija", Thickness.Low,
                                                                           [23, 3, 2021])
        package_of_disposable_tableware_obj_str = package_of_disposable_tableware_obj.__str__()
        correct_output = f'amount of pieces: 13 \n' \
                         f'origin country: Ukraine \n' \
                         f'type of dishes: Spoons \n' \
                         f'material: Paper \n' \
                         f'price: 45 \n' \
                         f'brand: Premija \n' \
                         f'thickness: Low \n' \
                         f'date of manufacture: [23, 3, 2021]'
        self.assertEqual(package_of_disposable_tableware_obj_str, correct_output)


class TestDrinkware(unittest.TestCase):
    def test__init__(self):
        drinkware_obj = Drinkware(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45,
                                  "Premija", Thickness.Low, [23, 3, 2021], 0.5, 95)
        assert drinkware_obj._amount_of_pieces == 13
        assert drinkware_obj._origin_country == Country.Ukraine
        assert drinkware_obj._type_of_dishes == Dishes.Spoons
        assert drinkware_obj._material == Material.Paper
        assert drinkware_obj._price == 45
        assert drinkware_obj._brand == "Premija"
        assert drinkware_obj._thickness == Thickness.Low
        assert drinkware_obj._date_of_manufacture == [23, 3, 2021]
        assert drinkware_obj._volume_in_litres == 0.5
        assert drinkware_obj._transparency_in_per_cents == 95
        self.assertTrue(0 < drinkware_obj._transparency_in_per_cents <= 100)

    def test__str__(self):
        drinkware_obj = Drinkware(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija",
                                  Thickness.Low, [23, 3, 2021], 0.5, 95)
        drinkware_obj_str = drinkware_obj.__str__()
        correct_output = f'amount of pieces: 13 \n' \
                         f'origin country: Ukraine \n' \
                         f'type of dishes: Spoons \n' \
                         f'material: Paper \n' \
                         f'price: 45 \n' \
                         f'brand: Premija \n' \
                         f'thickness: Low \n' \
                         f'date of manufacture: [23, 3, 2021]' \
                         f'\nvolume in litres: 0.5\n' \
                         f'transparency in per cents: 95\n'
        self.assertEqual(drinkware_obj_str, correct_output)


class TestSpoon(unittest.TestCase):
    def test__init__(self):
        spoon_obj = Spoon(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija", Thickness.Low,
                          [23, 3, 2021], 5, SpoonType.TableSpoon)
        assert spoon_obj._amount_of_pieces == 13
        assert spoon_obj._origin_country == Country.Ukraine
        assert spoon_obj._type_of_dishes == Dishes.Spoons
        assert spoon_obj._material == Material.Paper
        assert spoon_obj._price == 45
        assert spoon_obj._brand == "Premija"
        assert spoon_obj._thickness == Thickness.Low
        assert spoon_obj._date_of_manufacture == [23, 3, 2021]
        assert spoon_obj._length_in_inches == 5
        assert spoon_obj._spoon_type == SpoonType.TableSpoon


class TestFork(unittest.TestCase):
    def test__init__(self):
        fork_obj = Fork(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija", Thickness.Low,
                        [23, 3, 2021], 4.5, 3)
        assert fork_obj._amount_of_pieces == 13
        assert fork_obj._origin_country == Country.Ukraine
        assert fork_obj._type_of_dishes == Dishes.Spoons
        assert fork_obj._material == Material.Paper
        assert fork_obj._price == 45
        assert fork_obj._brand == "Premija"
        assert fork_obj._thickness == Thickness.Low
        assert fork_obj._date_of_manufacture == [23, 3, 2021]
        assert fork_obj._length_in_inches == 4.5
        assert fork_obj._prong_amount == 3


class TestPlate(unittest.TestCase):
    def test__init__(self):
        plate_obj = Plate(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija", Thickness.Low,
                          [23, 3, 2021], 15, 4, "red", "hearts")
        assert plate_obj._amount_of_pieces == 13
        assert plate_obj._origin_country == Country.Ukraine
        assert plate_obj._type_of_dishes == Dishes.Spoons
        assert plate_obj._material == Material.Paper
        assert plate_obj._price == 45
        assert plate_obj._brand == "Premija"
        assert plate_obj._thickness == Thickness.Low
        assert plate_obj._date_of_manufacture == [23, 3, 2021]
        assert plate_obj._diameter_in_cm == 15
        assert plate_obj._deepness_in_cm == 4
        assert plate_obj._color == "red"
        assert plate_obj._decoration == "hearts"


class TestGlass(unittest.TestCase):
    def test__init__(self):
        glass_obj = Glass(13, Country.Ukraine, Dishes.Spoons, Material.Paper, 45, "Premija", Thickness.Low,
                          [23, 3, 2021], 0.5, 80, "green", "dots")
        assert glass_obj._amount_of_pieces == 13
        assert glass_obj._origin_country == Country.Ukraine
        assert glass_obj._type_of_dishes == Dishes.Spoons
        assert glass_obj._material == Material.Paper
        assert glass_obj._price == 45
        assert glass_obj._brand == "Premija"
        assert glass_obj._thickness == Thickness.Low
        assert glass_obj._date_of_manufacture == [23, 3, 2021]
        assert glass_obj._volume_in_litres == 0.5
        assert glass_obj._transparency_in_per_cents == 80
        assert glass_obj._color == "green"
        assert glass_obj._decorations == "dots"


if __name__ == '__main__':
    unittest.main
