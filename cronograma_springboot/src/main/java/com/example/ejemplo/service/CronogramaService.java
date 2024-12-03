package com.example.ejemplo.service;




import javax.persistence.EntityNotFoundException;
import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.ejemplo.dto.CronogramaDTO;
import com.example.ejemplo.entities.CronogramaEntity;
import com.example.ejemplo.repository.CronogramaRepository;


import java.util.List;
import java.util.Optional;

@Service
public class CronogramaService {
    @Autowired
    private CronogramaRepository cronogramaRepository;

    @Transactional
    public CronogramaEntity createCronograma(CronogramaEntity cronograma) {
        return cronogramaRepository.save(cronograma);
    }

    @Transactional
    public List<CronogramaEntity> getAllCronogramas() {
        return cronogramaRepository.findAll();
    }

    @Transactional
    public Optional<CronogramaEntity> getCronogramaById(Long id) {
        return cronogramaRepository.findById(id);
    }


    @Transactional
    public CronogramaEntity updateCronograma(Long id, CronogramaEntity cronogramaDetails) {
        CronogramaEntity cronogramaEntity = cronogramaRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Cronograma not found with id " + id));

        cronogramaEntity.setNombre(cronogramaDetails.getNombre());
        cronogramaEntity.setDescripcion(cronogramaDetails.getDescripcion());
        // Set other fields as necessary

        return cronogramaRepository.save(cronogramaEntity);
    }

    @Transactional
    public void deleteCronograma(Long id) {
        Optional<CronogramaEntity> cronogramaEntity = cronogramaRepository.findById(id);
        
        if (!cronogramaEntity.isEmpty()) {
            cronogramaRepository.deleteById(id);
          }
          
        else {
            throw new EntityNotFoundException("Participante no encontrado");
        }
    }



}

