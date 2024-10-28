package com.inventario.web;

import com.inventario.domain.Listadeproducos;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import lombok.extern.slf4j.Slf4j;
import mx.inventario.dao.IlistadeproductosDAO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@Controller
@Slf4j
public class ControladorREST {
    
    @Autowired
    private IlistadeproductosDAO ilistadeproductosDAO;
    
    @GetMapping("/")
    public String comienzo(Model model) {
        
        Iterable<Listadeproducos> Listas = ilistadeproductosDAO.findAll();
        
        log.info("Estoy ejecutando el Controlador MVC");
        model.addAttribute("Listas", Listas);
        return "indice";
    }


}
