package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.entity.item.EveryScoreItem;
import com.homework.serverproject.service.EveryScoreService;
import com.homework.serverproject.service.TravelLineService;
import com.homework.serverproject.vo.EveryScoreVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class EveryScoreServiceImpl implements EveryScoreService {

    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<EveryScoreVo> geteveryscore() {
        List<EveryScoreVo> returnlist = new ArrayList<>();
        List<TravelLineEntity> tlist = new ArrayList<>();

        List<String> citynames = new ArrayList<>(Arrays.asList("changsha","chengdu","chongqing","dali","guangzhou","guiling","hangzhou","huangshan","hulunbeier","jiuzhaigou","kunming","lasa","lijiang","nanjing","qingdao","sanya","shanghai","suzhou","xiameng","xian","zhangjiajie"));
        for(String cityname : citynames){
            tlist = mongoTemplate.find(new Query(), TravelLineEntity.class,cityname);
            double allhotelexperience = 0;
            double allscheduling = 0;
            double alltourguide = 0;
            int count1 = 0;
            int count2 = 0;
            int count3 = 0;
            for(TravelLineEntity item : tlist){
                if(item.getEvery_item_rate().getHotelexperience()!=0){
                    allhotelexperience += item.getEvery_item_rate().getHotelexperience();
                    count1 ++;
                }
                if(item.getEvery_item_rate().getScheduling() != 0){
                    allscheduling += item.getEvery_item_rate().getScheduling();
                    count2 ++;
                }
                if(item.getEvery_item_rate().getTourguide() != 0){
                    alltourguide += item.getEvery_item_rate().getTourguide();
                    count3 ++;
                }
            }
            DecimalFormat df =new DecimalFormat("#0.000");
            Double format1 = Double.valueOf(df.format(allhotelexperience /count1));
            Double format2 = Double.valueOf(df.format(allscheduling / count2));
            Double format3 = Double.valueOf(df.format(alltourguide /count3));

            EveryScoreVo ev = new EveryScoreVo(cityname,format1,format2,format3);
            returnlist.add(ev);
        }

        return returnlist;


    }

}
