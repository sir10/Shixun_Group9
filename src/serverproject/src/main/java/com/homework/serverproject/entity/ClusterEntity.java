package com.homework.serverproject.entity;

import com.homework.serverproject.entity.item.ClusterRouteItem;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ClusterEntity {
    private String cluster_name;
    private List<ClusterRouteItem> tourist_route;
}
