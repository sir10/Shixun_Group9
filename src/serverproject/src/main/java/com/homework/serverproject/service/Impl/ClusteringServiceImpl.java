package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.ClusterEntity;
import com.homework.serverproject.entity.CommentEntity;
import com.homework.serverproject.service.ClusteringService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class ClusteringServiceImpl implements ClusteringService {

    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<ClusterEntity> getclusterresult(String cityname) {

        String queryname = cityname + "clustering";
        List<ClusterEntity> list = mongoTemplate.find(new Query(), ClusterEntity.class,queryname);
        return  list;
    }
}
