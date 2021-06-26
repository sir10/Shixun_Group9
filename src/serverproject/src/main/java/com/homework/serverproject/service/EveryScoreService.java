package com.homework.serverproject.service;

import com.homework.serverproject.entity.item.EveryScoreItem;
import com.homework.serverproject.vo.EveryScoreVo;

import java.util.List;

public interface EveryScoreService {
    List<EveryScoreVo> geteveryscore();
}
