package com.homework.serverproject.service;

import com.homework.serverproject.entity.CommentEntity;

import java.util.List;

public interface CommentService {

    List<CommentEntity> getcomment(String bookname);
}
