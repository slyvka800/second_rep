package ua.lviv.iot.disposable_tableware.models;

import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public class Plate extends PlatesAndBowls {
    private String color;
    private String decoration;
}
