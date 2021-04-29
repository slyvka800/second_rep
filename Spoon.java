package iot.ua;

import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
public  class Spoon extends Cutlery{
    private SpoonType spoonType;
}
