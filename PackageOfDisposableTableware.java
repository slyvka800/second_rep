package iot.ua;

import lombok.Data;
import lombok.ToString;
import lombok.experimental.SuperBuilder;

import  java.util.*;

@SuperBuilder
@Data
public abstract class PackageOfDisposableTableware {
    private int amountOfPieces;
    private Country originCountry;
    private Dishes type;
    private Material material;
    private float price;
    private String brand;
    private Thickness thickness;
    private int[] dateOfManufacture;
//    private List<Integer> dateOfManufacture;
//    private List<Integer> MyList = new ArrayList<Integer>();
}
