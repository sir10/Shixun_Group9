package com.homework.serverproject.vo;

import com.homework.serverproject.entity.item.EveryScoreItem;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class EveryScoreVo {
    private String cityname;
    private Double scheduling;
    private Double tourguide;
    private Double hotelexperience;
}
