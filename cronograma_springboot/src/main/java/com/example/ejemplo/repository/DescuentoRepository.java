package com.example.ejemplo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import org.springframework.stereotype.Repository;

import com.example.ejemplo.entities.DescuentoEntity;



@Repository
public interface DescuentoRepository extends JpaRepository<DescuentoEntity, Long>{

}
