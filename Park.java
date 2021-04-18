package ua.iot.lviv.parks;

public class Park {
    private String address;

    private int lengthOfBicycleLines;

    private int ticketPrice;

    private int quantityOfTrees;

    private String namedAfter;

    private int yearOfEstablishment;

    private boolean isAlcoholAllowed;

    private String dayOfDiscounts;

    private static int objectCount;

    protected String majorTree;

    protected boolean areDogsAllowed;

    public Park(String address, int lengthOfBicycleLines, int ticketPrice, int quantityOfTrees, String namedAfter,
                int yearOfEstablishment, boolean isAlcoholAllowed, String dayOfDiscounts, String majorTree,
                boolean areDogsAllowed) {
        setValues(address, lengthOfBicycleLines, ticketPrice, quantityOfTrees, namedAfter, yearOfEstablishment,
                isAlcoholAllowed, dayOfDiscounts, majorTree, areDogsAllowed);
        objectCount++;
    }

    public Park(int quantityOfTrees, String namedAfter, int yearOfEstablishment, boolean isAlcoholAllowed) {
        this(null, 0, 0, quantityOfTrees, namedAfter, yearOfEstablishment,
                isAlcoholAllowed, null, null, false);
    }

    public Park() {
        this(null, 0, 0, 0, null, 0,
                false,null, null, false);
    }

    public void resetValues(String address, int lengthOfBicycleLines, int ticketPrice, int quantityOfTrees,
                            String namedAfter, int yearOfEstablishment, boolean isAlcoholAllowed, String dayOfDiscounts,
                            String majorTree, boolean areDogsAllowed)
    {
        setValues(address, lengthOfBicycleLines, ticketPrice, quantityOfTrees, namedAfter, yearOfEstablishment,
                isAlcoholAllowed, dayOfDiscounts, majorTree, areDogsAllowed);
    }

    private void setValues(String address, int lengthOfBicycleLines, int ticketPrice, int quantityOfTrees,
                           String namedAfter, int yearOfEstablishment, boolean isAlcoholAllowed, String dayOfDiscounts,
                           String majorTree, boolean areDogsAllowed)
    {
        this.address = address;
        this.lengthOfBicycleLines = lengthOfBicycleLines;
        this.ticketPrice = ticketPrice;
        this.quantityOfTrees = quantityOfTrees;
        this.namedAfter = namedAfter;
        this.yearOfEstablishment = yearOfEstablishment;
        this.isAlcoholAllowed = isAlcoholAllowed;
        this.dayOfDiscounts = dayOfDiscounts;
        this.majorTree = majorTree;
        this.areDogsAllowed = areDogsAllowed;
    }

    public void printField() {
        System.out.println(objectCount);
    }

    public static void printStaticField() {
        System.out.println(objectCount);
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getLengthOfBicycleLines() {
        return lengthOfBicycleLines;
    }

    public void setLengthOfBicycleLines(int lengthOfBicycleLines) {
        this.lengthOfBicycleLines = lengthOfBicycleLines;
    }

    public int getTicketPrice() {
        return ticketPrice;
    }

    public void setTicketPrice(int ticketPrice) {
        this.ticketPrice = ticketPrice;
    }

    public int getQuantityOfTrees() {
        return quantityOfTrees;
    }

    public void setQuantityOfTrees(int quantityOfTrees) {
        this.quantityOfTrees = quantityOfTrees;
    }

    public String getNamedAfter() {
        return namedAfter;
    }

    public void setNamedAfter(String namedAfter) {
        this.namedAfter = namedAfter;
    }

    public int getYearOfEstablishment() {
        return yearOfEstablishment;
    }

    public void setYearOfEstablishment(int yearOfEstablishment) {
        this.yearOfEstablishment = yearOfEstablishment;
    }

    public boolean isAlcoholAllowed() {
        return isAlcoholAllowed;
    }

    public void setAlcoholAllowed(boolean alcoholAllowed) {
        isAlcoholAllowed = alcoholAllowed;
    }

    public String getDayOfDiscounts() {
        return dayOfDiscounts;
    }

    public void setDayOfDiscounts(String dayOfDiscounts) {
        this.dayOfDiscounts = dayOfDiscounts;
    }

    @Override
    public String toString() {
        return "Park [ address: " + address + "\nlength of bicycle lines: " + lengthOfBicycleLines + "\nticket price: "
                + ticketPrice + "\nquantity of trees: " + quantityOfTrees + "\nnamed after: " + namedAfter
                + "\nyear of establishment: " + yearOfEstablishment + "\nalcohol is allowed " + isAlcoholAllowed
                + "\nday of discount: " + dayOfDiscounts + "\nmajor tree: " + majorTree + "\ndogs are allowed: "
                + areDogsAllowed + " ]";
    }
}
