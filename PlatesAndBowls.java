package iot.ua;

import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public abstract class PlatesAndBowls extends PackageOfDisposableTableware{
    private int diameterInCm;
    private int deepnessInCm;
}
