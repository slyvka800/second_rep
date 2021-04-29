package iot.ua;

import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public class Plate extends PlatesAndBowls {
    private String color;
    private String decoration;
}
