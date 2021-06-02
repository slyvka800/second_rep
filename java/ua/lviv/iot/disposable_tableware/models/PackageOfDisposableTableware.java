/**
 * I have used here Date instead of int[] to store dateOfManufacture
 * because it is far more practical
 */
package ua.lviv.iot.disposable_tableware.models;

import lombok.Data;
import lombok.experimental.SuperBuilder;

import java.util.Date;

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
    private Date dateOfManufacture;

    protected PackageOfDisposableTableware() {
    }
}
