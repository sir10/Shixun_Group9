package com.homework.serverproject.service;

import com.homework.serverproject.vo.CityPopularityVo;
import com.homework.serverproject.vo.TravelPartnerVo;

import java.util.List;

public interface TravelPartnerService {
    List<TravelPartnerVo> getTravelPartner();
}
