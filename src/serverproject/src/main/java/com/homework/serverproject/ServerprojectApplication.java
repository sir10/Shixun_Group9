package com.homework.serverproject;

import com.homework.serverproject.controller.CommentController;
import com.homework.serverproject.service.CommentService;
import com.homework.serverproject.service.TravelLineService;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.mongodb.core.mapping.TextScore;

@SpringBootApplication
public class ServerprojectApplication {

    public static void main(String[] args) {
        SpringApplication.run(ServerprojectApplication.class, args);
    }

//    @Autowired
//    CommentService commentService;

//    @Test
//    public void test(){
//
//        System.out.println("xiyo");
//        System.out.println(commentService.getcomment("西游记"));
//    }
//    @Autowired
//    TravelLineService travelLineService;
//
//    @Test
//    public void test(){
//        System.out.println(travelLineService.getInfo());
//    }
}
