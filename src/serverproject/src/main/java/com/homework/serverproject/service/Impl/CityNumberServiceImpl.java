package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.service.CityNumberService;
import com.homework.serverproject.vo.CityNum;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class CityNumberServiceImpl implements CityNumberService {
    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<CityNum> getcitynum() {

        List<TravelLineEntity> list = new ArrayList<>();
        List<CityNum> returnlist = new ArrayList<>();
        List<String> citynames = new ArrayList<>(Arrays.asList("changsha","chengdu","chongqing","dali","guangzhou","guiling","hangzhou","huangshan","hulunbeier","jiuzhaigou","kunming","lasa","lijiang","nanjing","qingdao","sanya","shanghai","suzhou","xiameng","xian","zhangjiajie"));
        for(String cityname : citynames){
            list = mongoTemplate.find(new Query(), TravelLineEntity.class,cityname);
            if(list.size() > 2500) {
                CityNum c = new CityNum(cityname, list.size());
                returnlist.add(c);
            }



        }
        return returnlist;
    }
}
