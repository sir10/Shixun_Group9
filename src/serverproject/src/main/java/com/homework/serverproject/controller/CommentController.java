package com.homework.serverproject.controller;

import com.homework.serverproject.entity.CommentEntity;
import com.homework.serverproject.service.CommentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/api")
public class CommentController {
    @Autowired
    CommentService commentService;

    @GetMapping("/test/{bookname}")
    public List<CommentEntity> query(@PathVariable("bookname") String bookname) {
        System.out.println("访问成功");
        return commentService.getcomment(bookname);


    }

}
