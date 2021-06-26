package com.homework.serverproject.entity.item;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class EveryScoreItem {

    @Field("行程安排")
    private double scheduling;
    @Field("导游服务")
    private double tourguide;
    @Field("酒店体验")
    private double hotelexperience;

}
