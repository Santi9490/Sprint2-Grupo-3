package com.example.ejemplo.service;

import javax.persistence.EntityNotFoundException;
import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.ejemplo.entities.DescuentoEntity;
import com.example.ejemplo.repository.DescuentoRepository;

import java.util.List;
import java.util.Optional;

@Service
public class DescuentoService {
    @Autowired
    private DescuentoRepository descuentoRepository;

    @Transactional
    public DescuentoEntity createDescuento(DescuentoEntity descuento) {
        return descuentoRepository.save(descuento);
    }

    @Transactional
    public List<DescuentoEntity> getAllDescuentos() {
        return descuentoRepository.findAll();
    }

    @Transactional
    public Optional<DescuentoEntity> getDescuentoById(Long id) {
        return descuentoRepository.findById(id);
    }

    @Transactional
    public DescuentoEntity updateDescuento(Long id, DescuentoEntity descuentoDetails) {
        DescuentoEntity descuentoEntity = descuentoRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Descuento not found with id " + id));

        descuentoEntity.setDescripcion(descuentoDetails.getDescripcion());
        descuentoEntity.setPorcentaje(descuentoDetails.getPorcentaje());
        descuentoEntity.setActivo(descuentoDetails.getActivo());
        // Set other fields as necessary

        return descuentoRepository.save(descuentoEntity);
    }

    @Transactional
    public void deleteDescuento(Long id) {
        Optional<DescuentoEntity> descuentoEntity = descuentoRepository.findById(id);
        if (!descuentoEntity.isEmpty()) {
            descuentoRepository.deleteById(id);
        } else {
            throw new EntityNotFoundException("Descuento not found");
        }
    }
}
