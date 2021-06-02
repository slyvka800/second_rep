package ua.lviv.iot.disposable_tableware.models;

import lombok.Data;
import lombok.experimental.SuperBuilder;

import javax.persistence.Entity;


@Data
@SuperBuilder
@Entity
public abstract class Drinkware extends PackageOfDisposableTableware {


    private float volumeInLitres;
    private int transparencyInPerCents;

    protected Drinkware() {
        super();
    }

}
