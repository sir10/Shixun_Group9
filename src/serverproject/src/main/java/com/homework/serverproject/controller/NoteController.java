package com.homework.serverproject.controller;


import com.homework.serverproject.entity.NoteEntity;
import com.homework.serverproject.service.NoteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
public class NoteController {
    @Autowired
    NoteService noteService;

    @GetMapping("/note/{cityname}")
    public List<NoteEntity> query(@PathVariable("cityname") String cityname){
        System.out.println("访问成功");
        return noteService.getnote(cityname);
    }
}
