from manager.tableware_manager import *


class Testing:

    def main(self):
        package_of_glasses = Glass(10, Country.Ukraine, Dishes.Glass, Material.Wood, 35, "Coca-Cola", Thickness.Low,
                                   [23, 12, 2019], 0.5, 35, 'blue', 'stripes')
        package_of_spoons = Spoon(20, Country.China, Dishes.Spoons, Material.Wood, 100, "Nice Company",
                                  Thickness.High, [30, 12, 2021], 34, SpoonType.TableSpoon)
        package_of_forks = Fork(30, Country.Turkey, Dishes.Forks, Material.Plastic, 12, "Pepsi", Thickness.Low,
                                [6, 5, 2020], 34, 3)
        package_of_plates = Plate(40, Country.China, Dishes.Plates, Material.Paper, 130, "Cool company", Thickness.High,
                                  [6, 5, 2030], 12, 34, 'red', 'dots')
        package_of_glasses_second = Glass(50, Country.Turkey, Dishes.Glass, Material.Plastic, 35, "Good glass",
                                          Thickness.Medium, [3, 11, 2015], 1, 25, 'green', 'flowers')
        package_of_spoons_second = Spoon(60, Country.China, Dishes.Spoons, Material.Paper, 115, "Coca-Cola",
                                         Thickness.High, [31, 6, 2018], 45, SpoonType.TeaSpoon)
        package_of_forks_second = Fork(70, Country.Ukraine, Dishes.Forks, Material.Wood, 90, "Hot and Dog",
                                       Thickness.Medium, [15, 8, 2016], 6, 5)
        package_of_plates_second = Plate(80, Country.Turkey, Dishes.Plates, Material.Plastic, 130, "Jeremy`s co.",
                                         Thickness.Low, [28, 12, 2002], 68, 2.5, 'pink', 'hearts')

        manager = TablewareManager(package_of_glasses, package_of_spoons, package_of_forks, package_of_plates,
                                   package_of_glasses_second, package_of_spoons_second, package_of_forks_second,
                                   package_of_plates_second)

        print('\nSearch by material: wood\n')
        founds = manager.search_by_material(Material.Wood)
        for i in founds:
            print(i)


        print('\nDescending sort of plastic tableware by price:\n')
        sorted_found = manager.sort_selection_by_price(manager.search_by_material(Material.Plastic), SortOrder.DESC)
        for i in sorted_found:
            print(i)

        print('\nAscending sort of wooden tableware by date of manufacture:\n')
        sorted_found = manager.sort_selection_by_manufacture_date(manager.search_by_material(Material.Wood))
        for i in sorted_found:
            print(i)
