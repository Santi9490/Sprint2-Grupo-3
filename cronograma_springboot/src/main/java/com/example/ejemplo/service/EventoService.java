package com.example.ejemplo.service;

import javax.persistence.EntityNotFoundException;
import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.ejemplo.entities.EventosEntity;
import com.example.ejemplo.repository.EventosRepository;

import java.util.List;
import java.util.Optional;

@Service
public class EventoService {
    @Autowired
    private EventosRepository eventosRepository;

    @Transactional
    public EventosEntity createEvento(EventosEntity evento) {
        return eventosRepository.save(evento);
    }

    @Transactional
    public List<EventosEntity> getAllEventos() {
        return eventosRepository.findAll();
    }

    @Transactional
    public Optional<EventosEntity> getEventoById(Long id) {
        return eventosRepository.findById(id);
    }

    @Transactional
    public EventosEntity updateEvento(Long id, EventosEntity eventoDetails) {
        EventosEntity eventoEntity = eventosRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Evento not found with id " + id));

        eventoEntity.setNombre(eventoDetails.getNombre());
        eventoEntity.setDescripcion(eventoDetails.getDescripcion());
        // Set other fields as necessary

        return eventosRepository.save(eventoEntity);
    }

    @Transactional
    public void deleteEvento(Long id) {
        Optional<EventosEntity> eventoEntity = eventosRepository.findById(id);
        if (!eventoEntity.isEmpty()) {
            eventosRepository.deleteById(id);
        } else {
            throw new EntityNotFoundException("Evento not found");
        }
    }
}
