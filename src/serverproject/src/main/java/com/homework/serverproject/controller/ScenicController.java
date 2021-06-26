package com.homework.serverproject.controller;

import com.homework.serverproject.entity.ScenicEntity;
import com.homework.serverproject.service.ScenicService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
public class ScenicController {
    @Autowired
    ScenicService scenicService;

    @GetMapping("/scenic/{cityname}")
    public List<ScenicEntity> query(@PathVariable("cityname") String cityname) {
        System.out.println("访问成功");
        return scenicService.getscenic(cityname);
    }
}
