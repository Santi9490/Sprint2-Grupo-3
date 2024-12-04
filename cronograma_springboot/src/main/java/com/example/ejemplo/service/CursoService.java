package com.example.ejemplo.service;

import javax.persistence.EntityNotFoundException;
import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.ejemplo.entities.CursoEntity;
import com.example.ejemplo.repository.CursoRepository;

import java.util.List;
import java.util.Optional;

@Service
public class CursoService {
    @Autowired
    private CursoRepository cursoRepository;

    @Transactional
    public CursoEntity createCurso(CursoEntity curso) {
        return cursoRepository.save(curso);
    }

    @Transactional
    public List<CursoEntity> getAllCursos() {
        return cursoRepository.findAll();
    }

    @Transactional
    public Optional<CursoEntity> getCursoById(Long id) {
        return cursoRepository.findById(id);
    }

    @Transactional
    public CursoEntity updateCurso(Long id, CursoEntity cursoDetails) {
        CursoEntity cursoEntity = cursoRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Curso not found with id " + id));

        cursoEntity.setNombre(cursoDetails.getNombre());
        cursoEntity.setDescripcion(cursoDetails.getDescripcion());

        return cursoRepository.save(cursoEntity);
    }

    @Transactional
    public void deleteCurso(Long id) {
        Optional<CursoEntity> cursoEntity = cursoRepository.findById(id);
        if (!cursoEntity.isEmpty()) {
            cursoRepository.deleteById(id);
        } else {
            throw new EntityNotFoundException("Curso not found");
        }
    }
}
