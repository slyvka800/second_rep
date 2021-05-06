package iot.ua;

import lombok.Data;
import lombok.ToString;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public class Glass extends Drinkware{
    private String color;
    private String decoration;
}
