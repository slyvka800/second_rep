package iot.ua;

import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public class Forks extends Cutlery{
    private int prongAmount;
}
