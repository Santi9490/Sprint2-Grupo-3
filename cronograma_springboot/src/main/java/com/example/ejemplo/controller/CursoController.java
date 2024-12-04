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

import com.example.ejemplo.dto.CursoDTO;
import com.example.ejemplo.entities.CursoEntity;
import com.example.ejemplo.service.CursoService;

@RestController
@RequestMapping("/cursos")
public class CursoController {

    @Autowired
    private CursoService cursoService;

    @Autowired
    private ModelMapper modelMapper;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public CursoDTO createCurso(@RequestBody CursoDTO cursoDTO) {
        CursoEntity curso = modelMapper.map(cursoDTO, CursoEntity.class);
        return modelMapper.map(cursoService.createCurso(curso), CursoDTO.class);
    }

    @GetMapping
    public List<CursoDTO> getAllCursos() {
        List<CursoEntity> cursos = cursoService.getAllCursos();
        return modelMapper.map(cursos, new TypeToken<List<CursoDTO>>(){}.getType());
    }

    @GetMapping("/{id}")
    public CursoDTO getCursoById(@PathVariable Long id) {
        Optional<CursoEntity> curso = cursoService.getCursoById(id);
        return modelMapper.map(curso, CursoDTO.class);
    }

    @PutMapping("/{id}")
    public CursoDTO updateCurso(@PathVariable Long id, @RequestBody CursoDTO cursoDTO) {
        CursoEntity curso = modelMapper.map(cursoDTO, CursoEntity.class);
        return modelMapper.map(cursoService.updateCurso(id, curso), CursoDTO.class);
    }

    @DeleteMapping("/{id}")
    public void deleteCurso(@PathVariable Long id) {
        cursoService.deleteCurso(id);
    }
}
