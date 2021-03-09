from manager.tableware_manager import *


class Testing:

    def main(self):
        package1 = Glass(10, Country.Ukraine, Dishes.Glass, Material.Wood, 35, "Coca-Cola", Thickness.Low,
                         [23, 12, 2019],
                         0.5, 35, 'blue', 'stripes')
        package2 = Spoon(20, Country.China, Dishes.Spoons, Material.Wood, 100, "Nice Company",
                         Thickness.High, [30, 12, 2021], 34, SpoonType.TableSpoon)
        package3 = Fork(30, Country.Turkey, Dishes.Forks, Material.Plastic, 12, "Pepsi", Thickness.Low, [6, 5, 2020],
                        34, 3)
        package4 = Plate(40, Country.China, Dishes.Plates, Material.Paper, 130, "Cool company", Thickness.High,
                         [6, 5, 2030], 12, 34, 'red', 'dots')
        package5 = Glass(50, Country.Turkey, Dishes.Glass, Material.Plastic, 35, "Good glass", Thickness.Medium,
                         [3, 11, 2015],
                         1, 25, 'green', 'flowers')
        package6 = Spoon(60, Country.China, Dishes.Spoons, Material.Paper, 115, "Coca-Cola",
                         Thickness.High, [31, 6, 2018], 45, SpoonType.TeaSpoon)
        package7 = Fork(70, Country.Ukraine, Dishes.Forks, Material.Wood, 90, "Hot and Dog", Thickness.Medium,
                        [15, 8, 2016], 6, 5)
        package8 = Plate(80, Country.Turkey, Dishes.Plates, Material.Plastic, 130, "Jeremy`s co.", Thickness.Low,
                         [28, 12, 2002], 68, 2.5, 'pink', 'hearts')

        manager1 = TablewareManager(package1, package2, package3, package4, package5, package6, package7, package8)
        manager1.sortByPrice(SortOrder.ASC)
        print('Ascending sort by price:\n')
        print(manager1)

        print('Search by material: wood\n')
        manager1.searchByMaterial(Material.Wood)

        manager1.sortByManufactureDate(SortOrder.DESC)
        print('Descending sort by date of manufacture:\n')
        print(manager1)
