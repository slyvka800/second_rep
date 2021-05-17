package ua.lviv.iot.disposable_tableware.models;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
@AllArgsConstructor
public class Glass extends Drinkware{
    private int id;

    private String color;
    private String decoration;
}
