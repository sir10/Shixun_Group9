package com.homework.serverproject.service;



import com.homework.serverproject.entity.ScenicEntity;

import java.util.List;

public interface ScenicService {
    List<ScenicEntity> getscenic(String cityname);

}
