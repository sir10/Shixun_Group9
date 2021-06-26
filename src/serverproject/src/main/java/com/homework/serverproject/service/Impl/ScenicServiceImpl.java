package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.ScenicEntity;
import com.homework.serverproject.service.ScenicService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ScenicServiceImpl implements ScenicService {
    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<ScenicEntity> getscenic(String cityname) {
        String queryname = cityname + "travel_scenic";
        List<ScenicEntity> scenic = mongoTemplate.find(new Query(), ScenicEntity.class, queryname);
        return scenic;
    }
}
