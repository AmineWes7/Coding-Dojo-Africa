package com.Dojo_and_Ninjas.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/dojos")
public class DojoController {

    @Autowired
    private DojoRepository dojoRepository;

    @GetMapping("/new")
    public String newDojo() {
        return "newDojo";
    }

    @PostMapping("/create")
    public String createDojo(@RequestParam String name) {
        Dojo dojo = new Dojo(name);
        dojoRepository.save(dojo);
        return "redirect:/dojos";
    }

    @GetMapping
    public String listDojos(Model model) {
        List<Dojo> dojos = dojoRepository.findAll();
        model.addAttribute("dojos", dojos);
        return "dojos";
    }

    @GetMapping("/{id}")
    public String dojoDetails(@PathVariable Long id, Model model) {
        Dojo dojo = dojoRepository.findById(id).orElse(null);
        model.addAttribute("dojo", dojo);
        model.addAttribute("ninjas", dojo.getNinjas());
        return "dojoDetails";
    }
}