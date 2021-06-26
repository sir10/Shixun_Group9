package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.CommentEntity;
import com.homework.serverproject.service.CommentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CommentServiceImpl implements CommentService {

    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<CommentEntity> getcomment(String bookname) {
        Query query = Query.query(Criteria.where("book_name").is(bookname));
        List<CommentEntity> comment = mongoTemplate.find(query, CommentEntity.class);
        return comment;
    }
}
