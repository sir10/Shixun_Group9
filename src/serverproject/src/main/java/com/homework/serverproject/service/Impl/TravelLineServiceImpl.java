package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.CommentEntity;
import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.service.TravelLineService;
import com.homework.serverproject.vo.KeyWordVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class TravelLineServiceImpl implements TravelLineService {
    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<TravelLineEntity> getInfo() {

        List<TravelLineEntity> list = new ArrayList<>();
        List<String> citynames = new ArrayList<>(Arrays.asList("changsha","chengdu","chongqing","dali","guangzhou","guiling","hangzhou","huangshan","hulunbeier","jiuzhaigou","kunming","lasa","lijiang","nanjing","qingdao","sanya","shanghai","suzhou","xiameng","xian","zhangjiajie"));
        for(String cityname : citynames){
            list = mongoTemplate.find(new Query(), TravelLineEntity.class,cityname);
        }

        return list;
    }

    @Override
    public List<KeyWordVo> getkeywords(){

        Map<String,Integer> returnmap = new HashMap<>();

        List<TravelLineEntity> list = new ArrayList<>();
        List<String> citynames = new ArrayList<>(Arrays.asList("changsha","chengdu","chongqing","dali","guangzhou","guiling","hangzhou","huangshan","hulunbeier","jiuzhaigou","kunming","lasa","lijiang","nanjing","qingdao","sanya","shanghai","suzhou","xiameng","xian","zhangjiajie"));
        for(String cityname : citynames){
            list = mongoTemplate.find(new Query(), TravelLineEntity.class,cityname);
            for(TravelLineEntity item : list){
                List<String> keywords = item.getKeywords();
                for(String keyword : keywords){
                    if(!returnmap.containsKey(keyword))
                        returnmap.put(keyword,1);
                    else
                        returnmap.put(keyword,returnmap.get(keyword)+1);
                }
            }
        }

        List<KeyWordVo> returnlist = new ArrayList<>();
        Iterator<String> iter = returnmap.keySet().iterator();

        while(iter.hasNext()) {

            String key = iter.next();
            if(returnmap.get(key) > 100){
                KeyWordVo k = new KeyWordVo(key,returnmap.get(key));
                returnlist.add(k);
            }
        }

        return returnlist;


    }
}
