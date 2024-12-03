package com.example.ejemplo.entities;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
@Entity
@Setter
@Getter
public class CronogramaEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String descripcion;

    private Date dataInicio;

    private Date dataFin;

    private String status;

    private String nombre;

    
}
