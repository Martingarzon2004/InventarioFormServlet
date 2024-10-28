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

    global combo2
    combo2 =None

    global textBoxUbicacion
    textBoxUbicacion =None

    global textBoxNombre
    textBoxNombre =None

    global textBoxValorCompra
    textBoxValorCompra =None

    global boxIva
    boxIva =None

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

    global tree2
    tree2 =None

def Formulario():
        global textBoxId,combo,combo2,textBoxUbicacion,textBoxNombre,textBoxValorCompra,boxIva,textBoxCantidad,textBoxMinCantidad,textBoxFecha,textBoxComentarios,groupBox,tree
        try:
            base = Tk()
            base.geometry("1260x350")
            base.title("Formulario Python Unido")
            
            groupBox = ttk.Notebook(base)
            groupBox.grid(row=0,column=0,padx=5,pady=5)

            f1 = Frame(groupBox)
            groupBox.add(f1, text="Nuevo producto")

            textBoxId = Entry(f1)

            textBoxCantidad = Entry(f1)

            labelCategoria=Label(f1,text="Categorias:",width=10,font=("arial",10)).grid(row=1,column=0)
            seleccionCategoria = tk.StringVar()
            combo = ttk.Combobox(f1,values=["Papeleria","Cafeteria","Aseo"],textvariable=seleccionCategoria)
            combo.grid(row=1,column=1)

            labelUbicacion=Label(f1,text="Ubicación:",width=10,font=("arial",10)).grid(row=2,column=0)
            textBoxUbicacion = Entry(f1)
            textBoxUbicacion.grid(row=2,column=1)

            labelNombre=Label(f1,text="Nombre:",width=10,font=("arial",10)).grid(row=3,column=0)
            textBoxNombre = Entry(f1)
            textBoxNombre.grid(row=3,column=1)

            labelValorCompra=Label(f1,text="Valor Compra:",width=10,font=("arial",10)).grid(row=4,column=0)
            textBoxValorCompra = Entry(f1)
            textBoxValorCompra.grid(row=4,column=1)

            labelIva=Label(f1,text="Iva:",width=10,font=("arial",10)).grid(row=5,column=0)
            seleccionIva = tk.StringVar()
            boxIva = ttk.Combobox(f1,values=["N/A","5%","19%"],textvariable=seleccionIva)
            boxIva.grid(row=5,column=1)

            labelMinCantidad=Label(f1,text="Cantidad minima:",width=15,font=("arial",10)).grid(row=6,column=0)
            textBoxMinCantidad = Entry(f1)
            textBoxMinCantidad.grid(row=6,column=1)

            labelFecha=Label(f1,text="Fecha:",width=15,font=("arial",10)).grid(row=7,column=0)
            textBoxFecha = Entry(f1)
            textBoxFecha.grid(row=7,column=1)

            labelComentarios=Label(f1,text="Comentarios:",width=10,font=("arial",10)).grid(row=8,column=0)
            textBoxComentarios = Entry(f1)
            textBoxComentarios.grid(row=8,column=1)


            Button(f1,text="Nuevo",width=12,command=añadirRegistros).grid(row=9,column=0)
            Button(f1,text="Eliminar",width=10,command=eliminarRegistros).grid(row=9,column=1)


            ##f1a = Frame(groupBox)
            ##groupBox.add(f1a, text="Modificar")

            ##textBoxId = Entry(f1a)
            
            ##labelCategoria=Label(f1a,text="Categorias:",width=10,font=("arial",9)).grid(row=1,column=0)
            ##seleccionCategoria = tk.StringVar()
            ##combo = ttk.Combobox(f1a,values=["Papeleria","Cafeteria","Aseo"],textvariable=seleccionCategoria)
            ##combo.grid(row=1,column=1)

            ##labelUbicacion=Label(f1a,text="Ubicación:",width=10,font=("arial",9)).grid(row=2,column=0)
            ##textBoxUbicacion = Entry(f1a)
            ##textBoxUbicacion.grid(row=2,column=1)

            ##labelNombre=Label(f1a,text="Nombre:",width=10,font=("arial",9)).grid(row=3,column=0)
            ##textBoxNombre = Entry(f1a)
            ##textBoxNombre.grid(row=3,column=1)

            ##labelValorCompra=Label(f1a,text="Valor Compra:",width=10,font=("arial",9)).grid(row=4,column=0)
            ##textBoxValorCompra = Entry(f1a)
            ##textBoxValorCompra.grid(row=4,column=1)

            ##labelIva=Label(f1a,text="Iva:",width=10,font=("arial",9)).grid(row=5,column=0)
            ##textBoxIva = Entry(f1a)
            ##textBoxIva.grid(row=5,column=1)

            ##labelMinCantidad=Label(f1,text="Cantidad minima:",width=15,font=("arial",9)).grid(row=6,column=0)
            ##textBoxMinCantidad = Entry(f1a)
            ##textBoxMinCantidad.grid(row=6,column=1)

            ##labelFecha=Label(f1,text="Fecha:",width=15,font=("arial",9)).grid(row=7,column=0)
            ##textBoxFecha = Entry(f1a)
            ##textBoxFecha.grid(row=7,column=1)

            ##labelComentarios=Label(f1a,text="Comentarios:",width=10,font=("arial",9)).grid(row=8,column=0)
            ##textBoxComentarios = Entry(f1a)
            ##textBoxComentarios.grid(row=8,column=1)


            ##Button(f1a,text="Modificar",width=10,command=alterarRegistros).grid(row=9,column=0)


            f2 = Frame(groupBox)
            groupBox.add(f2, text="Entradas y Salidas")

            textBoxId = Entry(f2)

            ##textBoxNombre = Entry(f2)

            labelMovimiento=Label(f2,text="Tipo de movimiento:",width=15,font=("arial",9)).grid(row=1,column=0)
            seleccionMovimiento = tk.StringVar()
            combo2 = ttk.Combobox(f2,values=["Entrada","Salida"],textvariable=seleccionMovimiento)
            combo2.grid(row=1,column=1)

            labelCantidad=Label(f2,text="Cantidad:",width=10,font=("arial",9)).grid(row=2,column=0)
            textBoxCantidad = Entry(f2)
            textBoxCantidad.grid(row=2,column=1)

            labelFecha=Label(f2,text="Fecha:",width=15,font=("arial",9)).grid(row=3,column=0)
            textBoxFecha = Entry(f2)
            textBoxFecha.grid(row=3,column=1)

            labelComentarios=Label(f2,text="Comentarios:",width=10,font=("arial",9)).grid(row=4,column=0)
            textBoxComentarios = Entry(f2)
            textBoxComentarios.grid(row=4,column=1)


            Button(f2,text="Insertar movimiento",width=15,command=modificarRegistros).grid(row=5,column=0)
            

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
            
            groupBox = LabelFrame(base,text="Otras opciones",padx=2,pady=2)
            groupBox.grid(row=1,column=1,padx=2,pady=2)

            ##Button(groupBox,text="Refrescar tabla de inventario",width=24,command=actualizarTreeView).grid(row=0,column=0)
            Button(groupBox,text="Papelera de reciclaje",width=16,command=PapeleraDeReciclaje).grid(row=0,column=1)

            base.mainloop()
            
        except ValueError as error:
            print("Error al crear la interfaz: Error {}".format(error))

def añadirRegistros():
        global combo,textBoxUbicacion,textBoxNombre,textBoxValorCompra,boxIva,textBoxMinCantidad,textBoxFecha,textBoxComentarios,groupBox
        try:
            if combo is None or textBoxUbicacion is None or textBoxNombre is None or textBoxValorCompra is None or boxIva is None or textBoxMinCantidad is None or textBoxFecha is None or textBoxComentarios is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                return
            
            Categoria = combo.get()
            Ubicación = textBoxUbicacion.get()
            Nombre = textBoxNombre.get()
            ValorCompra = textBoxValorCompra.get()
            Iva = boxIva.get()
            MinCantidad = textBoxMinCantidad.get()
            Fecha = textBoxFecha.get()
            Comentarios = textBoxComentarios.get()

            print(Categoria)
            print(Ubicación)
            print(Nombre)
            print(ValorCompra)

            CProductos.ingresarProductos(Categoria,Ubicación,Nombre,ValorCompra,Iva,MinCantidad,Fecha,Comentarios)
            messagebox.showinfo("Información","Los datos fueron añadidos correctamente.")
            
            actualizarTreeView()

            
            combo.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxValorCompra.delete(0,END)
            boxIva.delete(0,END)
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
            textBoxId.delete(0,END)
            combo.delete(0,END)
            combo2.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxValorCompra.delete(0,END)
            boxIva.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxMinCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
            textBoxId.insert(0,values[0])
            textBoxUbicacion.insert(0,values[2])
            textBoxNombre.insert(0,values[3])
            textBoxValorCompra.insert(0,values[4])
            textBoxCantidad.insert(0,values[6])
            textBoxMinCantidad.insert(0,values[9])
            textBoxFecha.insert(0,values[11])
            textBoxComentarios.insert(0,values[13])
        
    except ValueError as error:
        print("Error al seleccionar datos: Error {}".format(error))

def alterarRegistros():
            global textBoxId,combo,textBoxUbicacion,textBoxNombre,textBoxValorCompra,boxIva,textBoxCantidad,textBoxMinCantidad,textBoxFecha,textBoxComentarios,groupBox
            try:
                if textBoxId is None or combo is None or textBoxUbicacion is None or textBoxNombre is None or textBoxValorCompra is None or boxIva is None or textBoxMinCantidad is None or textBoxFecha is None or textBoxComentarios is None:
                    print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                    return
                
                Id = textBoxId.get()
                Categoria = combo.get()
                Ubicación = textBoxUbicacion.get()
                Nombre = textBoxNombre.get()
                ValorCompra = textBoxValorCompra.get()
                Iva = boxIva.get()
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
                boxIva.delete(0,END)
                textBoxCantidad.delete(0,END)
                textBoxMinCantidad.delete(0,END)
                textBoxFecha.delete(0,END)
                textBoxComentarios.delete(0,END)
            
            except ValueError as error:
                print("Error al modificar los datos: Error {}".format(error))

def eliminarRegistros():
        global textBoxId
        try:
            if textBoxId is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                return
            
            Id = textBoxId.get()

            CProductos.eliminarProductos(Id)
            messagebox.showinfo("Información","Los datos fueron movidos a la papelera de Reciclaje.")
            
            actualizarTreeView()


            textBoxId.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos: Error {}".format(error))


def modificarRegistros():
        global textBoxId,combo2,textBoxNombre,textBoxCantidad,textBoxFecha,textBoxComentarios,groupBox
        try:
            if textBoxId is None or combo2 is None or textBoxNombre is None or textBoxCantidad is None or textBoxFecha is None or textBoxComentarios is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                print(textBoxId)
                print(combo2)
                print(textBoxNombre)
                print(textBoxCantidad)
                print(textBoxFecha)
                print(textBoxComentarios)
                return
            
            Id = textBoxId.get()
            Movimiento = combo2.get()
            Nombre = textBoxNombre.get()
            Cantidad = textBoxCantidad.get()
            Fecha = textBoxFecha.get()
            Comentarios = textBoxComentarios.get()

            print(Id)
            print(Movimiento)
            print(Nombre)
            print(Cantidad)
            print(Fecha)
            print(Comentarios)

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

def PapeleraDeReciclaje():
        global textBoxId,combo,textBoxUbicacion,textBoxNombre,textBoxValorCompra,boxIva,textBoxCantidad,textBoxMinCantidad,textBoxFecha,textBoxComentarios,groupBox,tree2
        try:
            window = tk.Toplevel(groupBox)
            window.grab_set()

            groupBox2 = LabelFrame(window,text="Papelera de reciclaje",padx=5,pady=5)
            groupBox2.grid(row=0,column=0,padx=5,pady=5)
            

            tree2 = ttk.Treeview(groupBox2,columns=("Id", "Categorias", "Ubicación", "Nombre",
            "Val.Compra", "Iva", "Entradas", "Salidas", "Stock", "Min.Cantidad", "Total sin IVA",
            "Fecha de inclución", "Fecha de modificación", "Comentarios"),selectmode="browse",
            show="headings", height=10)
            tree2.grid(row=1,column=1)

            tree2.column("# 1", width= 20, anchor=CENTER)
            tree2.heading("# 1",text="Id")

            tree2.column("# 2", width= 65, anchor=CENTER)
            tree2.heading("# 2",text="Categorias")

            tree2.column("# 3", width= 60, anchor=CENTER)
            tree2.heading("# 3",text="Ubicación")

            tree2.column("# 4", width= 120, anchor=CENTER)
            tree2.heading("# 4",text="Nombre")

            tree2.column("# 5", width= 70, anchor=CENTER)
            tree2.heading("# 5",text="Val.Compra")

            tree2.column("# 6", width= 30, anchor=CENTER)
            tree2.heading("# 6",text="Iva")

            tree2.column("# 7", width= 55, anchor=CENTER)
            tree2.heading("# 7",text="Entradas")

            tree2.column("# 8", width= 45, anchor=CENTER)
            tree2.heading("# 8",text="Salidas")

            tree2.column("# 9", width= 40, anchor=CENTER)
            tree2.heading("# 9",text="Stock")

            tree2.column("# 10", width= 60, anchor=CENTER)
            tree2.heading("# 10",text="Min.Cantidad")

            tree2.column("# 11", width= 70, anchor=CENTER)
            tree2.heading("# 11",text="Total sin Iva")
            
            tree2.column("# 12", width= 95, anchor=CENTER)
            tree2.heading("# 12",text="Fecha inclución")

            tree2.column("# 13", width= 115, anchor=CENTER)
            tree2.heading("# 13",text="Fecha modificación")

            tree2.column("# 14", width= 80, anchor=CENTER)
            tree2.heading("# 14",text="Comentarios")



            for row in CProductos.mostrarPapelera():
                tree2.insert("","end",values=row)
            
            



            tree2.bind("<<TreeviewSelect>>",seleccionarPapelera)
            
            
            scrollbar2 = Scrollbar(groupBox2, orient="vertical", command=tree2.yview)
            tree2.configure(yscrollcommand=scrollbar2.set)

            tree2.pack(side=LEFT)
            scrollbar2.pack(side=RIGHT,  fill="y")
            tree2.bind("<MouseWheel>", lambda event: tree2.yview_scroll(-1 * int((event.delta / 120)), "units"))
            

            groupBox2 = LabelFrame(window,text="Opciones",padx=5,pady=5)
            groupBox2.grid(row=1,column=0,padx=5,pady=5)
            Button(groupBox2,text="Regresar producto al inventario",width=30,command=eliminarPapelera).grid(row=0,column=0)

        except ValueError as error:
            print("Error al modificar los datos: Error {}".format(error))

def actualizarTreePapelera():
    global tree2

    try:
        tree2.delete(*tree2.get_children())

        datos = CProductos.mostrarPapelera()

        for row in CProductos.mostrarPapelera():
            tree.insert("","end",values=row)
    
    except ValueError as error:
        print("Error al actualizar la tabla: Error {}".format(error))

def eliminarPapelera():
        global textBoxId
        try:
            if textBoxId is None:
                print("Datos incompletos. Porfavor, rellene todos los campos de datos")
                return
            
            Id = textBoxId.get()

            CProductos.sacarPapelera(Id)
            messagebox.showinfo("Información","Los datos fueron movidos al inventario principal.")
            
            actualizarTreePapelera()


            textBoxId.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos: Error {}".format(error))

def seleccionarPapelera(event):
    try:
        seleccion = tree2.focus()
        if seleccion:
            values = tree2.item(seleccion)["values"]
            textBoxId.delete(0,END)
            combo.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxValorCompra.delete(0,END)
            boxIva.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxMinCantidad.delete(0,END)
            textBoxFecha.delete(0,END)
            textBoxComentarios.delete(0,END)
            textBoxId.insert(0,values[0])
            textBoxUbicacion.insert(0,values[2])
            textBoxNombre.insert(0,values[3])
            textBoxValorCompra.insert(0,values[4])
            textBoxMinCantidad.insert(0,values[9])
            textBoxFecha.insert(0,values[11])
            textBoxComentarios.insert(0,values[13])
        
    except ValueError as error:
        print("Error al seleccionar datos: Error {}".format(error))


Formulario()