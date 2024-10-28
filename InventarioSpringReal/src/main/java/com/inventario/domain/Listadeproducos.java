package com.inventario.domain;

import java.io.Serializable;
import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "listadeproductos")
public class Listadeproducos implements Serializable {
    private static final long serialVersionUID = 1L;
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long Id;
    private String Nombre;
    private String Cantidad;
    private String Tipodeproducto;
    private String Localizacion;
    private String Preciodeventa;
}
