package com.homework.serverproject.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class PoemEntity {
    private String keyword;
    private ArrayList<String> content;
}
