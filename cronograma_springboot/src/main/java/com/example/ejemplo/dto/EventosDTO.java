package com.example.ejemplo.dto;

import java.time.LocalDate;

import com.example.ejemplo.entities.CronogramaEntity;

import lombok.Data;

@Data
public class EventosDTO {

    private Long id;
    private String nombre;
    private String descripcion;
    private LocalDate fecha;
    private String status;
    private Boolean obligatorio;

    private CronogramaEntity cronograma;

}
