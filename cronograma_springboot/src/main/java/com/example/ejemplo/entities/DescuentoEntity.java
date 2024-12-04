package com.example.ejemplo.entities;

import java.math.BigDecimal;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Data
@Entity
@Setter
@Getter
public class DescuentoEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre; // Ej. "Descuento por pronto pago"
    private BigDecimal porcentaje; // Ej. 10%
    private String activo;
    private String descripcion; // Ej. "Descuento por pronto pago del 10%"

    private CronogramaEntity CronogramaEntity;

    // Getters y Setters
    
}
