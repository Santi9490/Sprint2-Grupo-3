package com.example.ejemplo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.ejemplo.entities.EventosEntitity;

import org.springframework.stereotype.Repository;

@Repository
public interface EventosRepository extends JpaRepository<EventosEntitity, Long>  {

}
