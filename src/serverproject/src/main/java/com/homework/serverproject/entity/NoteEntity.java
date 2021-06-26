package com.homework.serverproject.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class NoteEntity {
    private String title;
    private String content;
    private String like;
    private String comments;
    private String url;
}
