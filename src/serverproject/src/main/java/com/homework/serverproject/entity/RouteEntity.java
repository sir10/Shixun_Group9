package com.homework.serverproject.entity;


import com.homework.serverproject.entity.item.RealRouteItem;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.lang.annotation.Documented;
import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
//@Documented(collection = "city_router")
public class RouteEntity {
    private String recommend_route;
    private List<RealRouteItem> real_route;
}
