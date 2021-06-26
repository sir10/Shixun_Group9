package com.homework.serverproject.service;



import com.homework.serverproject.entity.RouteEntity;

import java.util.List;

public interface RouteService {
    List<RouteEntity> getroute(String cityname);

}
