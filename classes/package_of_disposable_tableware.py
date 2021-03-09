from enum import Enum


class Country(Enum):
    Ukraine = 1
    China = 2
    Turkey = 3


class Material(Enum):
    Paper = 1
    Plastic = 2
    Wood = 3


class Thickness(Enum):
    High = 1
    Medium = 2
    Low = 3


class Dishes(Enum):
    Plates = 1
    Spoons = 2
    Forks = 3
    Knifes = 4
    PaperCups = 5
    Straws = 6
    Glass = 7


class PackageOfDisposableTableware:
    def __init__(self, amount_of_pieces, origin_country: Country, type_of_dishes: Dishes, material: Material, price,
                 brand, thickness: Thickness, date_of_manufacture: list):
        self._amount_of_pieces = amount_of_pieces
        self._origin_country = origin_country
        self._type_of_dishes = type_of_dishes
        self._material = material
        self._price = price
        self._brand = brand
        self._thickness = thickness
        self._date_of_manufacture = date_of_manufacture

    def __str__(self):
        return f'amount of pieces: {self._amount_of_pieces} \n' \
               f'origin country: {self._origin_country.name} \n' \
               f'type of dishes: {self._type_of_dishes.name} \n' \
               f'material: {self._material.name} \n' \
               f'price: {self._price} \n' \
               f'brand: {self._brand} \n' \
               f'thickness: {self._thickness.name} \n' \
               f'date of manufacture: {self._date_of_manufacture}'
