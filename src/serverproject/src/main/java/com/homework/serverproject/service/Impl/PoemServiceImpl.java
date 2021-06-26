package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.PoemEntity;
import com.homework.serverproject.service.PoemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PoemServiceImpl implements PoemService {
    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<PoemEntity> getpoem(String keyword) {
        Query query = Query.query(Criteria.where("keyword").is(keyword));
        List<PoemEntity> poem = mongoTemplate.find(query, PoemEntity.class, "travel_poem");
        return poem;
    }
}
