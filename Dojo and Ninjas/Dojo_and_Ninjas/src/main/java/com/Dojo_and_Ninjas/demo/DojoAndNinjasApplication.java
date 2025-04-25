package com.Dojo_and_Ninjas.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/ninjas")
public class NinjaController {

    @Autowired
    private NinjaRepository ninjaRepository;

    @Autowired
    private DojoRepository dojoRepository;

    @GetMapping("/new")
    public String newNinja(Model model) {
        model.addAttribute("dojos", dojoRepository.findAll());
        return "newNinja";
    }

    @PostMapping("/create")
    public String createNinja(@RequestParam String name, @RequestParam String beltColor, @RequestParam Long dojoId) {
        Dojo dojo = dojoRepository.findById(dojoId).orElse(null);
        Ninja ninja = new Ninja(name, beltColor, dojo);
        ninjaRepository.save(ninja);
        return "redirect:/dojos";
    }
}