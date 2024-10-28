# importar modulos para UI
import tkinter as tk



from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from tkinter import Scrollbar

from conexion import *

from productos import *
# importar otros modulos

class FormularioInventario:

    global textBoxId
    textBoxId =None

    global combo
    combo =None

    global textBoxUbicacion
    textBoxUbicacion =None

    global textBoxNombre
    textBoxNombre =None

    global textBoxValorCompra
    textBoxValorCompra =None

    global textBoxIva
    textBoxIva =None

    global textBoxCantidad
    textBoxCantidad =None

    global textBoxMinCantidad
    textBoxMinCantidad =None

    global textBoxFecha
    textBoxFecha =None

    global textBoxComentarios
    textBoxComentarios =None

    global groupBox
    groupBox =None

    global tree
    tree =None

def Formulario():
        global textBoxId
        global combo
        global textBoxUbicacion
        global textBoxNombre
        global textBoxValorCompra
        global textBoxIva
        global textBoxCantidad
        global textBoxMinCantidad
        global textBoxFecha
        global textBoxComentarios
        global groupBox
        global tree
        try:
            base = Tk()
            base.geometry("1260x350")
            base.title("Formulario Python")
            
            textBoxId = Entry(groupBox)

            groupBox = LabelFrame(base,text="Creacion de nuevos productos",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=5,pady=5)

            labelCategoria=Label(groupBox,text="Categorias:",width=10,font=("arial",9)).grid(row=1,column=0)
            seleccionCategoria = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Papeleria","Cafeteria","Aseo"],textvariable=seleccionCategoria)
            combo.grid(row=1,column=1)

            labelUbicacion=Label(groupBox,text="Ubicación:",width=10,font=("arial",9)).grid(row=2,column=0)
            textBoxUbicacion = Entry(groupBox)
            textBoxUbicacion.grid(row=2,column=1)

            labelNombre=Label(groupBox,text="Nombre:",width=10,font=("arial",9)).grid(row=3,column=0)
            textBoxNombre = Entry(groupBox)
            textBoxNombre.grid(row=3,column=1)

            labelValorCompra=Label(groupBox,text="Valor Compra:",width=10,font=("arial",9)).grid(row=4,column=0)
            textBoxValorCompra = Entry(groupBox)
            textBoxValorCompra.grid(row=4,column=1)

            labelIva=Label(groupBox,text="Iva:",width=10,font=("arial",9)).grid(row=5,column=0)
            textBoxIva = Entry(groupBox)
            textBoxIva.grid(row=5,column=1)

            labelCantidad=Label(groupBox,text="Cantidad:",width=10,font=("arial",9)).grid(row=6,column=0)
            textBoxCantidad = Entry(groupBox)
            textBoxCantidad.grid(row=6,column=1)

            labelMinCantidad=Label(groupBox,text="Cantidad minima:",width=15,font=("arial",9)).grid(row=7,column=0)
            textBoxMinCantidad = Entry(groupBox)
            textBoxMinCantidad.grid(row=7,column=1)

            labelFecha=Label(groupBox,text="Fecha:",width=15,font=("arial",9)).grid(row=8,column=0)
            textBoxFecha = Entry(groupBox)
            textBoxFecha.grid(row=8,column=1)

            labelComentarios=Label(groupBox,text="Comentarios:",width=10,font=("arial",9)).grid(row=9,column=0)
            textBoxComentarios = Entry(groupBox)
            textBoxComentarios.grid(row=9,column=1)


            Button(groupBox,text="Añadir",width=15,command=añadirRegistros).grid(row=10,column=0)
            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=11,column=0)
            Button(groupBox,text="Eliminar",width=10).grid(row=10,column=1)
            # Este boton debe esatr bloqueado por defecto.


            groupBox = LabelFrame(base,text="Inventario",padx=5,pady=5)
            groupBox.grid(row=0,column=1,padx=5,pady=5)

            tree = ttk.Treeview(groupBox,columns=("Id", "Categorias", "Ubicación", "Nombre",
            "Val.Compra", "Iva", "Entradas", "Salidas", "Stock", "Min.Cantidad", "Total sin IVA",
            "Fecha de inclución", "Fecha de modificación", "Comentarios"),selectmode="browse",
            show="headings", height=10)
            tree.grid(row=1,column=1)

            tree.column("# 1", width= 20, anchor=CENTER)
            tree.heading("# 1",text="Id")

            tree.column("# 2", width= 65, anchor=CENTER)
            tree.heading("# 2",text="Categorias")

            tree.column("# 3", width= 60, anchor=CENTER)
            tree.heading("# 3",text="Ubicación")

            tree.column("# 4", width= 120, anchor=CENTER)
            tree.heading("# 4",text="Nombre")

            tree.column("# 5", width= 70, anchor=CENTER)
            tree.heading("# 5",text="Val.Compra")

            tree.column("# 6", width= 30, anchor=CENTER)
            tree.heading("# 6",text="Iva")

            tree.column("# 7", width= 55, anchor=CENTER)
            tree.heading("# 7",text="Entradas")

            tree.column("# 8", width= 45, anchor=CENTER)
            tree.heading("# 8",text="Salidas")

            tree.column("# 9", width= 40, anchor=CENTER)
            tree.heading("# 9",text="Stock")

            tree.column("# 10", width= 60, anchor=CENTER)
            tree.heading("# 10",text="Min.Cantidad")

            tree.column("# 11", width= 70, anchor=CENTER)
            tree.heading("# 11",text="Total sin Iva")
            
            tree.column("# 12", width= 95, anchor=CENTER)
            tree.heading("# 12",text="Fecha inclución")

            tree.column("# 13", width= 115, anchor=CENTER)
            tree.heading("# 13",text="Fecha modificación")

            tree.column("# 14", width= 80, anchor=CENTER)
            tree.heading("# 14",text="Comentarios")



            for row in CProductos.mostrarProductos():
                tree.insert("","end",values=row)
            
            



            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
            
            
            scrollbar1 = Scrollbar(groupBox, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar1.set)
            ##scrollbar1.grid(column=2,row=1,sticky="ns")


            tree.pack(side=LEFT)
            ##scrollbar2 = Scrollbar(groupBox, orient="horizontal", command=tree.xview)
            ##scrollbar1.grid(column=2,row=1,sticky="ns")
            ##scrollbar2.grid(column=1,row=2)
            scrollbar1.pack(side=RIGHT,  fill="y")
            ##scrollbar2.pack(side=BOTTOM,  fill="x")
            ##tree.configure(yscrollcommand=scrollbar1.set)
            ##tree.configure(xscrollcommand=scrollbar2.set)
            tree.bind("<MouseWheel>", lambda event: tree.yview_scroll(-1 * int((event.delta / 120)), "units"))

            base.mainloop()
            
            
        except ValueError as error:
            print("Error al crear la interfaz: Error {}".format(error))

def añadirRegistros():
        global combo,textBoxUbicacion,textBoxNombre,textBoxValorCompra,textBoxIva,textBoxCantidad,textBoxMinCantidad,textBoxFecha,textBoxComentarios,groupBox
        try:
            if combo is None or textBoxUbicacion is None or textBoxNombre is None or textBoxValorCompra is None or textBoxIva is None or textBoxCantidad is None or textBoxMinCantidad is None or textBoxFecha is None or textBoxComentarios is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                return
            
            Categoria = combo.get()
            Ubicación = textBoxUbicacion.get()
            Nombre = textBoxNombre.get()
            ValorCompra = textBoxValorCompra.get()
            Iva = textBoxIva.get()
            Cantidad = textBoxCantidad.get()
            MinCantidad = textBoxMinCantidad.get()
            Fecha = textBoxFecha.get()
            Comentarios = textBoxComentarios.get()

            CProductos.ingresarProductos(Categoria,Ubicación,Nombre,ValorCompra,Iva,Cantidad,MinCantidad,Fecha,Comentarios)
            messagebox.showinfo("Información","Los datos fueron añadidos correctamente.")
            
            actualizarTreeView()

            
            combo.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxValorCompra.delete(0,END)
            textBoxIva.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxMinCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
        
        except ValueError as error:
            print("Error al añadir nuevos datos: Error {}".format(error))

def actualizarTreeView():
    global tree

    try:
        tree.delete(*tree.get_children())

        datos = CProductos.mostrarProductos()

        for row in CProductos.mostrarProductos():
            tree.insert("","end",values=row)
    
    except ValueError as error:
        print("Error al actualizar la tabla: Error {}".format(error))

def seleccionarRegistro(event):
    try:
        seleccion = tree.focus()
        if seleccion:
            values = tree.item(seleccion)["values"]
            combo.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxValorCompra.delete(0,END)
            textBoxIva.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxMinCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
            textBoxId.insert(0,values[0])
            combo.set(values[1])
            textBoxUbicacion.insert(0,values[2])
            textBoxNombre.insert(0,values[3])
            textBoxValorCompra.insert(0,values[4])
            textBoxIva.insert(0,values[5])
            ##textBoxCantidad.insert(0,values[6])
            textBoxMinCantidad.insert(0,values[9])
            textBoxFecha.insert(0,values[11])
            textBoxComentarios.insert(0,values[13])
        
    except ValueError as error:
        print("Error al seleccionar datos: Error {}".format(error))


def modificarRegistros():
        global textBoxId,combo,textBoxUbicacion,textBoxNombre,textBoxValorCompra,textBoxIva,textBoxMinCantidad,textBoxFecha,textBoxComentarios,groupBox
        try:
            if textBoxId is None or combo is None or textBoxUbicacion is None or textBoxNombre is None or textBoxValorCompra is None or textBoxIva is None or textBoxMinCantidad is None or textBoxFecha is None or textBoxComentarios is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                return
            
            Id = textBoxId.get()
            Categoria = combo.get()
            Ubicación = textBoxUbicacion.get()
            Nombre = textBoxNombre.get()
            ValorCompra = textBoxValorCompra.get()
            Iva = textBoxIva.get()
            MinCantidad = textBoxMinCantidad.get()
            Fecha = textBoxFecha.get()
            Comentarios = textBoxComentarios.get()

            CProductos.modificarProductos(Id,Categoria,Ubicación,Nombre,ValorCompra,Iva,MinCantidad,Fecha,Comentarios)
            messagebox.showinfo("Información","Los datos fueron añadidos correctamente.")
            
            actualizarTreeView()


            textBoxId.delete(0,END)
            combo.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxValorCompra.delete(0,END)
            textBoxIva.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxMinCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos: Error {}".format(error))


def eliminarRegistros():
        global textBoxId,combo,textBoxUbicacion,textBoxNombre,textBoxValorCompra,textBoxIva,textBoxCantidad,textBoxMinCantidad,textBoxFecha,textBoxComentarios,groupBox
        try:
            if textBoxId is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                return
            
            Id = textBoxId.get()

            CProductos.modificarProductos(Id)
            messagebox.showinfo("Información","Los datos fueron eliminados correctamente.")
            
            actualizarTreeView()


            textBoxId.delete(0,END)
            combo.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxValorCompra.delete(0,END)
            textBoxIva.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxMinCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos: Error {}".format(error))


Formulario()