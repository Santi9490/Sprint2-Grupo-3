package com.example.ejemplo.repository;

import org.springframework.data.jpa.repository.JpaRepository;


import org.springframework.stereotype.Repository;

import com.example.ejemplo.entities.EventosEntity;

@Repository
public interface EventosRepository extends JpaRepository<EventosEntity, Long>  {

}
