package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.service.CityPriceService;
import com.homework.serverproject.vo.CityPriceVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class CityPriceServiceImpl implements CityPriceService {

    @Autowired
    MongoTemplate mongoTemplate;

    public double getonecityprice(String cityname){
        List<TravelLineEntity> list = mongoTemplate.find(new Query(), TravelLineEntity.class, cityname);
        double allprice = 0;
        for(TravelLineEntity item : list){
            allprice += item.getPrice();
        }

        return allprice / list.size();
    }

    @Override
    public List<CityPriceVo> getcityprice() {
        List<CityPriceVo> resultlist = new ArrayList<>();
        List<String> citynames = new ArrayList<>(Arrays.asList("changsha","chengdu","chongqing","dali","guangzhou","guiling","hangzhou","huangshan","hulunbeier","jiuzhaigou","kunming","lasa","lijiang","nanjing","qingdao","sanya","shanghai","suzhou","xiameng","xian","zhangjiajie"));
        for(String cityname : citynames){
            int price = (int) getonecityprice(cityname);
            CityPriceVo c = new CityPriceVo(cityname,price);
            resultlist.add(c);
        }
        return resultlist;
    }
}
