package com.homework.serverproject.entity;

import com.homework.serverproject.entity.item.EveryScoreItem;
import com.homework.serverproject.entity.item.RouteCommentItem;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Field;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class TravelLineEntity {
    @Field("线路名")
    private String routename;
    @Field("编号")
    private int id;
    @Field("url")
    private String url;
    @Field("供应商")
    private String supplier;
    @Field("钻数")
    private double star;
    @Field("行程")
    private List<String> everyroute;
    @Field("酒店")
    private List<String> hotel;
    @Field("总评分")
    private Double score;
    @Field("好评率")
    private Double praise_rate;
    @Field("各项评分")
    private EveryScoreItem every_item_rate;
    @Field("关键词")
    private List<String> keywords;
    @Field("评论")
    private List<RouteCommentItem> commentInfo;
    @Field("价格")
    private double price;




}
