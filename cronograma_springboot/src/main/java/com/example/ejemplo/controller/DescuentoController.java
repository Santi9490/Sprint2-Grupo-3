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

import com.example.ejemplo.dto.DescuentoDTO;
import com.example.ejemplo.entities.DescuentoEntity;
import com.example.ejemplo.service.DescuentoService;

@RestController
@RequestMapping("/descuentos")
public class DescuentoController {

    @Autowired
    private DescuentoService descuentoService;

    @Autowired
    private ModelMapper modelMapper;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public DescuentoDTO createDescuento(@RequestBody DescuentoDTO descuentoDTO) {
        DescuentoEntity descuento = modelMapper.map(descuentoDTO, DescuentoEntity.class);
        return modelMapper.map(descuentoService.createDescuento(descuento), DescuentoDTO.class);
    }

    @GetMapping
    public List<DescuentoDTO> getAllDescuentos() {
        List<DescuentoEntity> descuentos = descuentoService.getAllDescuentos();
        return modelMapper.map(descuentos, new TypeToken<List<DescuentoDTO>>(){}.getType());
    }

    @GetMapping("/{id}")
    public DescuentoDTO getDescuentoById(@PathVariable Long id) {
        Optional<DescuentoEntity> descuento = descuentoService.getDescuentoById(id);
        return modelMapper.map(descuento, DescuentoDTO.class);
    }

    @PutMapping("/{id}")
    public DescuentoDTO updateDescuento(@PathVariable Long id, @RequestBody DescuentoDTO descuentoDTO) {
        DescuentoEntity descuento = modelMapper.map(descuentoDTO, DescuentoEntity.class);
        return modelMapper.map(descuentoService.updateDescuento(id, descuento), DescuentoDTO.class);
    }

    @DeleteMapping("/{id}")
    public void deleteDescuento(@PathVariable Long id) {
        descuentoService.deleteDescuento(id);
    }
}
