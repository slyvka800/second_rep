package ua.lviv.iot.disposable_tableware.models;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");

        Glass glass = null;
        try {
            glass = Glass.builder()
                    .color("red")
                    .brand("cocacola")
                    .amountOfPieces(5)
                    .type(Dishes.Glasses)
                    .decoration("dots")
                    .dateOfManufacture(dateFormat.parse("28-12-2002"))
                    .material(Material.Paper)
                    .originCountry(Country.Ukraine)
                    .price(45)
                    .thickness(Thickness.Low)
                    .volumeInLitres(0.5F)
                    .transparencyInPerCents(20)
                    .build();
        } catch (ParseException e) {
            e.printStackTrace();
        }

        Spoon spoon = null;
        try {
            spoon = Spoon.builder()
                    .spoonType(SpoonType.TableSpoon)
                    .price(23)
                    .amountOfPieces(45)
                    .thickness(Thickness.High)
                    .dateOfManufacture(dateFormat.parse("23-11-2020"))
                    .brand("Domdom")
                    .originCountry(Country.Ukraine)
                    .build();
        } catch (ParseException e) {
            e.printStackTrace();
        }
        Plate plate = null;
        try {
            plate = Plate.builder()
                    .color("red")
                    .decoration("stripes")
                    .diameterInCm(2)
                    .dateOfManufacture(dateFormat.parse("23-10-2020"))
                    .price(120)
                    .build();
        } catch (ParseException e) {
            e.printStackTrace();
        }
        Forks fork = null;
        try {
            fork = Forks.builder()
                    .dateOfManufacture(dateFormat.parse("10-02-2021"))
                    .price(15)
                    .brand("Coconut Co.")
                    .material(Material.Paper)
                    .build();
        } catch (ParseException e) {
            e.printStackTrace();
        }

        List<PackageOfDisposableTableware> listOfItems = new ArrayList<PackageOfDisposableTableware>();
        listOfItems.add(glass);
        listOfItems.add(spoon);
        listOfItems.add(plate);
        listOfItems.add(fork);

        TablewareManager manager = TablewareManager.builder().items(listOfItems).build();

        System.out.println(listOfItems);
        manager.sortByDate(listOfItems, SortOrder.ASC);
        System.out.println(listOfItems);
        System.out.println(manager.searchByMaterial(Material.Paper));

    }
}
