package iot.ua;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args)
    {
        var glass = Glass.builder()
                .color("red")
                .brand("cocacola")
                .amountOfPieces(5)
                .type(Dishes.Glasses)
                .decoration("dots")
                .dateOfManufacture(new int[] {12, 3, 2021})
                .material(Material.Paper)
                .originCountry(Country.Ukraine)
                .price(45)
                .thickness(Thickness.Low)
                .volumeInLitres(0.5F)
                .transparencyInPerCents(20)
                .build();

        var spoon = Spoon.builder()
                .spoonType(SpoonType.TableSpoon)
                .price(23)
                .amountOfPieces(45)
                .thickness(Thickness.High)
                .dateOfManufacture(new int[] {1, 5, 2020})
                .brand("Domdom")
                .originCountry(Country.Ukraine)
                .build();
        var plate = Plate.builder()
                .color("red")
                .decoration("stripes")
                .diameterInCm(2)
                .dateOfManufacture(new int[] {12, 2, 2021})
                .price(120)
                .build();
        var fork = Forks.builder()
                .dateOfManufacture(new int[] {7, 8, 2019})
                .price(15)
                .brand("Coconut Co.")
                .material(Material.Paper)
                .build();

        List<PackageOfDisposableTableware> listOfItems = new ArrayList<PackageOfDisposableTableware>();
        listOfItems.add(glass);
        listOfItems.add(spoon);
        listOfItems.add(plate);
        listOfItems.add(fork);
        TablewareManager manager = new TablewareManager(listOfItems);

        System.out.println(listOfItems);
        manager.sortByDate(listOfItems, SortOrder.ASC);
        System.out.println(listOfItems);

    }
}
