/**
 * I have used here Date instead of int[] to store dateOfManufacture
 * because it is far more practical
 */
package ua.lviv.iot.disposable_tableware.models;

import lombok.Data;
import lombok.experimental.SuperBuilder;

import javax.persistence.*;
import java.util.Date;

@SuperBuilder
@Data
@MappedSuperclass
public abstract class PackageOfDisposableTableware {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;

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
