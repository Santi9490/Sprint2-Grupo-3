package com.example.ejemplo.entities;


import java.time.LocalDate;
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
public class CursoEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;
    private String descripcion;

    //@OneToMany(mappedBy = "student", cascade = CascadeType.ALL)

    
    // Getters y Setters
}

