package com.example.ejemplo.controller;


import java.util.List;
import java.util.Optional;

import org.modelmapper.ModelMapper;
import org.modelmapper.TypeToken;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.example.ejemplo.dto.CronogramaDTO;
import com.example.ejemplo.entities.CronogramaEntity;
import com.example.ejemplo.service.CronogramaService;


@RestController
@RequestMapping("/cronogramas")
public class CronogramaController {

    @Autowired
    private CronogramaService cronogramaService;

    @Autowired
    private ModelMapper modelMapper;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public CronogramaDTO createCronograma(@RequestBody CronogramaDTO cronogramaDTO) {
        CronogramaEntity cronograma = modelMapper.map(cronogramaDTO, CronogramaEntity.class);
        return modelMapper.map(cronogramaService.createCronograma(cronograma), CronogramaDTO.class);
    }

    @GetMapping
    public List<CronogramaDTO> getAllCronogramas() {
        List<CronogramaEntity> cronogramas = cronogramaService.getAllCronogramas();
        return modelMapper.map(cronogramas, new TypeToken<List<CronogramaDTO>>() {
        }.getType());
    }

    @GetMapping("/{id}")
    public CronogramaDTO getCronogramaById(@PathVariable Long id) {
        Optional<CronogramaEntity> cronograma = cronogramaService.getCronogramaById(id);
      //          .orElseThrow(() -> new ResourceNotFoundException("Cronograma not found for this id :: " + id));
        return modelMapper.map(cronograma, CronogramaDTO.class);
    }

    @PutMapping("/{id}")
    public CronogramaDTO updateCronograma(@PathVariable Long id, @RequestBody CronogramaDTO cronogramaDTO) {
        CronogramaEntity cronograma = modelMapper.map(cronogramaDTO, CronogramaEntity.class);
        return modelMapper.map(cronogramaService.updateCronograma(id, cronograma), CronogramaDTO.class);
    }

    @DeleteMapping("/{id}")
    public void deleteCronograma(@PathVariable Long id) {
        cronogramaService.deleteCronograma(id);
    }
    
    
}

