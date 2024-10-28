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

    global textBoxNombre
    textBoxNombre =None

    global textBoxCantidad
    textBoxCantidad =None

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
        global textBoxNombre
        global textBoxCantidad
        global textBoxFecha
        global textBoxComentarios
        global groupBox
        global tree
        try:
            base = Tk()
            base.geometry("1260x350")
            base.title("Modulo de movimientos (Entradas y salidas)")

            textBoxId = Entry(groupBox)

            textBoxNombre = Entry(groupBox)

            groupBox = LabelFrame(base,text="Entradas y Salidas de productos",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=5,pady=5)

            labelMovimiento=Label(groupBox,text="Tipo de movimiento:",width=15,font=("arial",9)).grid(row=1,column=0)
            seleccionMovimiento = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Entrada","Salida"],textvariable=seleccionMovimiento)
            combo.grid(row=1,column=1)

            labelCantidad=Label(groupBox,text="Cantidad:",width=10,font=("arial",9)).grid(row=2,column=0)
            textBoxCantidad = Entry(groupBox)
            textBoxCantidad.grid(row=2,column=1)

            labelFecha=Label(groupBox,text="Fecha:",width=15,font=("arial",9)).grid(row=3,column=0)
            textBoxFecha = Entry(groupBox)
            textBoxFecha.grid(row=3,column=1)

            labelComentarios=Label(groupBox,text="Comentarios:",width=10,font=("arial",9)).grid(row=4,column=0)
            textBoxComentarios = Entry(groupBox)
            textBoxComentarios.grid(row=4,column=1)


            Button(groupBox,text="Insertar movimiento",width=15,command=modificarRegistros).grid(row=5,column=0)


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
            textBoxCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
            textBoxId.insert(0,values[0])
            textBoxNombre.insert(0,values[1])
            ##textBoxCantidad.insert(0,values[6])
            ##textBoxFecha.insert(0,values[11])
            textBoxComentarios.insert(0,values[13])
        
    except ValueError as error:
        print("Error al seleccionar datos: Error {}".format(error))


def modificarRegistros():
        global textBoxId,combo,textBoxNombre,textBoxCantidad,textBoxFecha,textBoxComentarios,groupBox
        try:
            if textBoxId is None or combo is None or textBoxNombre is None or textBoxCantidad is None or textBoxFecha is None or textBoxComentarios is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                return
            
            Id = textBoxId.get()
            Movimiento = combo.get()
            Nombre = textBoxNombre.get()
            Cantidad = textBoxCantidad.get()
            Fecha = textBoxFecha.get()
            Comentarios = textBoxComentarios.get()

            if Movimiento=="Entrada":
                print("Haciendo una entrada")
                CProductos.añadirEntradas(Id,Nombre,Cantidad,Fecha,Comentarios)
            elif Movimiento=="Salida":
                print("Haciendo una salida")
                CProductos.añadirSalidas(Id,Nombre,Cantidad,Fecha,Comentarios)
            messagebox.showinfo("Información","El movimiento fue realizado correctamente.")
            
            actualizarTreeView()


            textBoxId.delete(0,END)
            combo.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos: Error {}".format(error))


Formulario()