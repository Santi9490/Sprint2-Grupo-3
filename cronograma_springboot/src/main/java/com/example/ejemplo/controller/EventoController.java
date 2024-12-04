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

import com.example.ejemplo.dto.EventosDTO;
import com.example.ejemplo.entities.EventosEntity;
import com.example.ejemplo.service.EventoService;

@RestController
@RequestMapping("/eventos")
public class EventoController {

    @Autowired
    private EventoService eventoService;

    @Autowired
    private ModelMapper modelMapper;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public EventosDTO createEvento(@RequestBody EventosDTO eventoDTO) {
        EventosEntity evento = modelMapper.map(eventoDTO, EventosEntity.class);
        return modelMapper.map(eventoService.createEvento(evento), EventosDTO.class);
    }

    @GetMapping
    public List<EventosDTO> getAllEventos() {
        List<EventosEntity> eventos = eventoService.getAllEventos();
        return modelMapper.map(eventos, new TypeToken<List<EventosDTO>>(){}.getType());
    }

    @GetMapping("/{id}")
    public EventosDTO getEventoById(@PathVariable Long id) {
        Optional<EventosEntity> evento = eventoService.getEventoById(id);
        return modelMapper.map(evento, EventosDTO.class);
    }

    @PutMapping("/{id}")
    public EventosDTO updateEvento(@PathVariable Long id, @RequestBody EventosDTO eventoDTO) {
        EventosEntity evento = modelMapper.map(eventoDTO, EventosEntity.class);
        return modelMapper.map(eventoService.updateEvento(id, evento), EventosDTO.class);
    }

    @DeleteMapping("/{id}")
    public void deleteEvento(@PathVariable Long id) {
        eventoService.deleteEvento(id);
    }
}
