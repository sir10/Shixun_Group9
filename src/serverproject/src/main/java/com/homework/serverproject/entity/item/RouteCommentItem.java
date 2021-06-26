package com.homework.serverproject.entity.item;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class RouteCommentItem {
    @Field("用户名")
    private String name;
    @Field("同行")
    private String partner;
    @Field("时间")
    private String time;
    @Field("用户评分")
    private double score;
    @Field("评论")
    private String comment;
}
