package com.homework.serverproject.vo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class CityPriceVo {

    private String cityname;
    private int averageprice;
}
