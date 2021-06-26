package com.homework.serverproject.service;



import com.homework.serverproject.entity.PoemEntity;

import java.util.List;

public interface PoemService {
    List<PoemEntity> getpoem(String keyword);
}
