package com.homework.serverproject.service;



import com.homework.serverproject.entity.NoteEntity;

import java.util.List;

public interface NoteService {
    List<NoteEntity> getnote(String cityname);
}
