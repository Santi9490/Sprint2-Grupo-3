package com.example.ejemplo.dto;

import java.math.BigDecimal;

import com.example.ejemplo.entities.CronogramaEntity;

import lombok.Data;

@Data
public class DescuentoDTO {

    private Long id;
    private String nombre; // Ej. "Descuento por pronto pago"
    private BigDecimal porcentaje; // Ej. 10%
    private String activo;
    private String descripcion; // Ej. "Descuento por pronto pago del 10%"

    private CronogramaEntity CronogramaEntity;

}
