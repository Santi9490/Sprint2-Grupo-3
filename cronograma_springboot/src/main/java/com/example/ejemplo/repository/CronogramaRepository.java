package com.example.ejemplo.repository;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.ejemplo.entities.CronogramaEntity;

@Repository
public interface CronogramaRepository extends JpaRepository<CronogramaEntity, Long>{


}
