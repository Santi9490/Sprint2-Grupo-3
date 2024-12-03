package com.example.ejemplo.dto;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
public class CronogramaDTO {
    private Long id;
    private String descripcion;

    private Date dataInicio;

    private Date dataFin;

    private String status;

    private String nombre;

}
