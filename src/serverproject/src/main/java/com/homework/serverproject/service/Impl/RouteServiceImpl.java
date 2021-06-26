package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.RouteEntity;
import com.homework.serverproject.service.RouteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import java.util.List;

@Service
public class RouteServiceImpl implements RouteService {
    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<RouteEntity> getroute(String cityname) {
        String queryname = cityname + "travel_route";
        List<RouteEntity> route = mongoTemplate.find(new Query(), RouteEntity.class,queryname);
        return route;
    }


}
