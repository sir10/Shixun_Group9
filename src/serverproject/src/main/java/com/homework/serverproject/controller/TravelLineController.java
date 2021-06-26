package com.homework.serverproject.controller;

import com.homework.serverproject.entity.ClusterEntity;
import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.entity.item.EveryScoreItem;
import com.homework.serverproject.service.*;
import com.homework.serverproject.vo.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@CrossOrigin
@RestController
public class TravelLineController {
    @Autowired
    TravelLineService travelLineService;

    @Autowired
    TravelPartnerService cityService;

    @Autowired
    CityPriceService cityPriceService;

    @Autowired
    CityPopularityService cityPopularityService;

    @Autowired
    ClusteringService clusteringService;

    @Autowired
    EveryScoreService everyScoreService;

    @Autowired
    CityNumberService cityNumberService;

    @GetMapping("/keyi")
    public List<TravelLineEntity> query(){
        return travelLineService.getInfo();
    }

    @GetMapping("/citypopularity")
    public List<CityPopularityVo> getCPV(){
        return cityPopularityService.getCityPopularity();

    }

    @GetMapping("/travelpartner")
    public List<TravelPartnerVo> getTPV(){
        return cityService.getTravelPartner();
    }

    @GetMapping("/cityprice")
    public List<CityPriceVo> getCP(){
        return cityPriceService.getcityprice();
    }

    @CrossOrigin
    @GetMapping("/cluster/{cityname}")
    public  List<ClusterEntity> getcluster(@PathVariable("cityname") String cityname){
        return clusteringService.getclusterresult(cityname);
    }

    @GetMapping("/everyscore")
    public List<EveryScoreVo> geteveryscore(){
        return everyScoreService.geteveryscore();
    }

    @GetMapping("/keyword")
    public List<KeyWordVo> getkeywords(){
        return travelLineService.getkeywords();
    }

    @GetMapping("/map")
    public List<CityNum> getcitynum(){
        return cityNumberService.getcitynum();
    }
}
