package com.homework.serverproject.service;

import com.homework.serverproject.entity.TravelLineEntity;
import com.homework.serverproject.vo.KeyWordVo;

import java.util.List;
import java.util.Map;

public interface TravelLineService {
    List<TravelLineEntity> getInfo();
    List<KeyWordVo> getkeywords();
}
