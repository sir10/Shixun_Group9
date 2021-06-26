package com.homework.serverproject.controller;

import com.homework.serverproject.entity.PoemEntity;
import com.homework.serverproject.service.PoemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
public class PoemController {
    @Autowired
    PoemService poemService;

    @GetMapping("/poem/{keyword}")
    public List<PoemEntity> query(@PathVariable("keyword") String keyword) {
        System.out.println("访问成功");
        return poemService.getpoem(keyword);
    }
}
