package ua.lviv.iot.disposable_tableware.models;

import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public abstract class Cutlery extends PackageOfDisposableTableware {
    private float lengthInInches;
}
