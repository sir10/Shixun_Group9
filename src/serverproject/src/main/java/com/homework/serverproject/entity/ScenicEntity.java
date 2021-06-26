package com.homework.serverproject.entity;


import com.homework.serverproject.entity.item.ScenicCommentItem;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Field;

import java.util.ArrayList;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ScenicEntity {
    private String url;
    private String name;
    private String rank;
    private ArrayList<String> picurl;
    private String address;
    private String introduction;
    private String time;
    private String traffic;
    private Double score;
    private ArrayList<String> keyword;
    private ArrayList<ScenicCommentItem> comments;
}
