package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.service.CityPopularityService;
import com.homework.serverproject.vo.CityPopularityVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class CityPopularityServiceImpl implements CityPopularityService {

    @Autowired
    MongoTemplate mongoTemplate;

    public double getOneCityPopularity(String cityname){

        List<TravelLineEntity> list = mongoTemplate.find(new Query(), TravelLineEntity.class,cityname);
        double allScore = 0;
        int count = 0;
        for(TravelLineEntity item : list){
            if(item.getScore() == -1.0){

            }
            else {
                allScore += item.getScore() * 0.8 + item.getStar() * 0.2;
                count ++;
            }
        }

        DecimalFormat df =new DecimalFormat("#0.00");
        Double format = Double.valueOf(df.format(allScore / count));

        return format;
    }


    public List<CityPopularityVo> getCityPopularity() {

        List<CityPopularityVo> returndatalist = new ArrayList<>();
        List<String> citynames = new ArrayList<>(Arrays.asList("changsha","chengdu","chongqing","dali","guangzhou","guiling","hangzhou","huangshan","hulunbeier","jiuzhaigou","kunming","lasa","lijiang","nanjing","qingdao","sanya","shanghai","suzhou","xiameng","xian","zhangjiajie"));
        for(String cityname : citynames){

            double oneCityPopularity = getOneCityPopularity(cityname);
            CityPopularityVo c = new CityPopularityVo(cityname,oneCityPopularity);
            returndatalist.add(c);
        }

        return returndatalist;


    }
}
