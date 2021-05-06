/** I have used here Calendar instead of int[] to store dateOfManufacture
 * because it is far more practical
 */
package iot.ua;

import lombok.Data;
import lombok.experimental.SuperBuilder;
import java.util.Calendar;

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
    private Calendar dateOfManufacture;
//    private List<Integer> dateOfManufacture;
//    private List<Integer> MyList = new ArrayList<Integer>();
}
