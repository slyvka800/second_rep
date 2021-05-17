package ua.lviv.iot.disposable_tableware.models;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.experimental.SuperBuilder;

import java.util.Calendar;

@Data
@SuperBuilder
public abstract class Drinkware extends PackageOfDisposableTableware {


    private float volumeInLitres;
    private int transparencyInPerCents;

    protected Drinkware(){
        super();
    }

//    protected Drinkware(float volumeInLitres, int transparencyInPerCents, int amountOfPieces, Country originCountry,
//                      Dishes type, Material material, float price, String brand, Thickness thickness,
//                      Calendar dateOfManufacture) {
//        super(amountOfPieces, originCountry, type, material, price, brand, thickness, dateOfManufacture);
//        this.volumeInLitres = volumeInLitres;
//        this.transparencyInPerCents = transparencyInPerCents;
//    }
}
