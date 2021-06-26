package com.homework.serverproject.service.Impl;

import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.entity.item.RouteCommentItem;
import com.homework.serverproject.service.TravelPartnerService;
import com.homework.serverproject.vo.TravelPartnerVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class TravelPartnerServiceImpl implements TravelPartnerService {

    @Autowired
    MongoTemplate mongoTemplate;

    @Override
    public List<TravelPartnerVo> getTravelPartner() {
        List<TravelPartnerVo> resultList = new ArrayList<TravelPartnerVo>();
        Map<String,Integer> partnerNumMap = new HashMap<String,Integer>();
        List<String> citynames = new ArrayList<>(Arrays.asList("changsha","chengdu","chongqing","dali","guangzhou","guiling","hangzhou","huangshan","hulunbeier","jiuzhaigou","kunming","lasa","lijiang","nanjing","qingdao","sanya","shanghai","suzhou","xiameng","xian","zhangjiajie"));
        for(String cityname : citynames) {
            List<TravelLineEntity> travelLines = mongoTemplate.find(new Query(), TravelLineEntity.class, cityname);
            for (TravelLineEntity travelLine : travelLines) {
                List<RouteCommentItem> commentInfos = travelLine.getCommentInfo();
                for (RouteCommentItem commentInfo : commentInfos) {
                    if (!partnerNumMap.containsKey(commentInfo.getPartner())) {
                        partnerNumMap.put(commentInfo.getPartner(), 1);
                    } else {
                        Integer value = partnerNumMap.get(commentInfo.getPartner());
                        partnerNumMap.put(commentInfo.getPartner(), value + 1);
                    }
                }
            }
        }

        for (String key : partnerNumMap.keySet()) {
            TravelPartnerVo travelPartnervo = new TravelPartnerVo();
            travelPartnervo.setPartnertype(key);
            travelPartnervo.setNumber(partnerNumMap.get(key));
            resultList.add(travelPartnervo);
        }


        return resultList;
    }
}

