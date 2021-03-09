from classes.package_of_disposable_tableware import *
from classes.plates_and_bowls import *
from classes.cutlery import *
from classes.drinkware import *
from classes.plate import *
from classes.spoon_and_fork import *
from classes.glass import *

from time import mktime
from enum import Enum


class SortOrder(Enum):
    ASC = False
    DESC = True


class TablewareManager(object):
    def __init__(self, *args: PackageOfDisposableTableware):
        self.packages = list(args)
        self.list_of_find = []
        self.output_list = []
        self.output_str: str

    def sortByPrice(self, sort_order=SortOrder.ASC):
        self.packages.sort(key=lambda item: item._price, reverse=sort_order.value)

    def sortByManufactureDate(self, sort_order=SortOrder.ASC):

        def time_converter(package: PackageOfDisposableTableware):
            time_tuple = (package._date_of_manufacture[2], package._date_of_manufacture[1],
                          package._date_of_manufacture[0], 0, 0, 0, 0, 0, 0)
            return mktime(time_tuple)

        self.packages.sort(key=lambda package: time_converter(package), reverse=sort_order.value)

    def searchByMaterial(self, material: Material):

        def find_material(package: PackageOfDisposableTableware):
            if package._material == material:
                self.list_of_find.append(package)

        for item in self.packages:
            find_material(item)

        return list(map(print, self.list_of_find))

    def __str__(self):
        self.output_str = ''
        for item in self.packages:
            self.output_str += item.__str__() + '\n'
        return self.output_str
