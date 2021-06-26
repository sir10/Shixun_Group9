package com.homework.serverproject.controller;

import com.homework.serverproject.entity.RouteEntity;
import com.homework.serverproject.service.RouteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
public class RouteController {
    @Autowired
    RouteService routeService;

    @GetMapping("/route/{cityname}")
    public List<RouteEntity> query(@PathVariable("cityname") String cityname) {
        System.out.println("访问成功");
        return routeService.getroute(cityname);
    }

}
