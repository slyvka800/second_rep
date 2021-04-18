package ua.iot.lviv.parks;

public class Main {

    public static void main(String[] args)
    {
        Park parkShevchenka = new Park(890, "Taras Shevchenko", 1910,
                false);
        System.out.println(parkShevchenka);
        parkShevchenka.printField();

        Park centralPark = new Park("Main Avenue", 35000, 450, 78000,
                "Center", 1850, true, "Sunday",
                "American Elm", true);
        System.out.println(centralPark);
        centralPark.printField();

        Park yosemiteNationalPark = new Park();
        System.out.println(yosemiteNationalPark);
        yosemiteNationalPark.printField();

        Park.printStaticField();
    }

}
