/** I have used here Calendar instead of int[] to store dateOfManufacture
 * because it is far more practical
 */
package ua.lviv.iot.disposable_tableware.models;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.experimental.SuperBuilder;

import java.util.Calendar;

@SuperBuilder
@Data
//@AllArgsConstructor
public abstract class PackageOfDisposableTableware {
    private int amountOfPieces;
    private Country originCountry;
    private Dishes type;
    private Material material;
    private float price;
    private String brand;
    private Thickness thickness;
    private Calendar dateOfManufacture;

    protected PackageOfDisposableTableware(){}
//    private List<Integer> dateOfManufacture;
//    private List<Integer> MyList = new ArrayList<Integer>();
}
