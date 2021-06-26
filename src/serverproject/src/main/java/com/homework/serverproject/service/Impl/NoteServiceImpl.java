package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.NoteEntity;
import com.homework.serverproject.service.NoteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NoteServiceImpl implements NoteService {
    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<NoteEntity> getnote(String cityname) {
        String queryname = cityname + "travel_notes";
        List<NoteEntity> list = mongoTemplate.find(new Query(), NoteEntity.class,queryname);
        return list;
    }
}
