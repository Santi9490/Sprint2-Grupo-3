package com.example.ejemplo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.ejemplo.entities.DescuentoEntitity;
import org.springframework.stereotype.Repository;

@Repository
public interface DescuentoRepository extends JpaRepository<DescuentoEntitity, Long>{

}
