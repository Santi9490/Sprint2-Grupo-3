package com.example.ejemplo.dto;

import java.util.Date;

import lombok.Data;

@Data
public class CronogramaDTO {
    private Long id;
    private String descripcion;

    private Date dataInicio;

    private Date dataFin;

    private String status;

    private String nombre;


}
