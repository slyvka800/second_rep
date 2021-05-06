package iot.ua;

import lombok.Data;
import lombok.ToString;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public abstract class Drinkware extends PackageOfDisposableTableware{
    private float volumeInLitres;
    private int transparencyInPerCents;
}
