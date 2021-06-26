package com.homework.serverproject.service;

import com.homework.serverproject.entity.ClusterEntity;

import java.util.List;

public interface ClusteringService {
    List<ClusterEntity> getclusterresult(String cityname);
}
