package com.Dojo_and_Ninjas.demo;

import org.springframework.data.jpa.repository.JpaRepository;

public interface NinjaRepository extends JpaRepository<Ninja, Long> {
}