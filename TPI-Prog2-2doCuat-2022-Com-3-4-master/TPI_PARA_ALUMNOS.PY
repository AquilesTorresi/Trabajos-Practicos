from ast import If
from datetime import date
import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("########__MENU DE OPCIONES DE LA CONCESIONARIA__#########")
            print("1)-------->  Cargar Monopatin  <-------------------------")
            print("2)-------->  Modificar Monopatin  <----------------------")
            print("3)-------->  Borrar Monopatin  <-------------------------")
            print("4)-------->  Carga la disponibilidad  <------------------")
            print("5)-------->  Mostrar producto  <-------------------------")
            print("6)-------->  Actualizar precios a dolar  <---------------")
            print("7)-------->  Mostarar datos hasta la fecha ingresada  <--")
            print("8)::::::::::::::::::__CREAR TABLA__::::::::::::::::::::::")
            print("9):::::::::::__BORRAR TODOS LOS DATOS__::::::::::::::::::")
            print("0)==============>  Salir de menu  <======================") #SIEMPRE Q QUIERAS RESTABLECER INGRESAR LOS Nº 9 Y 8 EN ESE ORDEN
            nro = int(input("Por favor ingrese un número: "))
            if nro == 1:
                modelo = input("Por favor ingrese el modelo del Monopatin: ")
                marca = input("Por favor ingrese la marca del Monopatin: ")
                potencia = input("Por favor ingrese la potencia del Monopatin: ")
                precio = input("Por favor ingrese el precio del Monopatin: ")
                color = input("Por favor ingrese el color del Monopatin: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                fechaUltimoPrecio = date.today()
                nuevo_monopatin = monopatin(modelo,marca,potencia,precio,color,cantidadDisponibles,fechaUltimoPrecio)
                nuevo_monopatin.cargar_monopatin()
            if nro == 2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                precio = float(input("Por favor ingrese el nuevo precio: "))
                monopatin.modificar_monopatin(self, marca, precio)
            if nro == 3:
                marca = input("Por favor ingrese la marca del Monopatin: ")
                monopatin.borrar_monopatin(self, marca)
            if nro == 4:
                marca = str(input("por favor ingrese la marca para cargar el stock: "))
                monopatin.cargar_stock(self, marca)    
            if nro == 5:
                monopatin.mostrar(self)
            if nro == 6:
                actualizarAdolar: float = 0.23
                sql = "UPDATE MONOPATIN SET precio=precio+(precio*'{}') ".format(actualizarAdolar)
                conexion = Conexiones()
                conexion.abrirConexion()
                try:
                    conexion.miCursor.execute(sql)
                    conexion.miConexion.commit()
                    conexion.miCursor.execute("SELECT * FROM HISTORICA")
                    datos = conexion.miCursor.fetchall()
                    for i in datos:
                        print(i)
                except:
                    print("Error")
                finally:
                    conexion.cerrarConexion()
            if nro == 7:
                anio = str(input("Ingrese el año: "))
                mes = str(input("Ingrese el mes: "))
                dia = str(input("Ingrese el dia: "))
                fecha_usuario = date(int(anio), int(mes), int(dia))
                fecha_cero = date(1000,3,3)
                conexion = Conexiones()
                conexion.abrirConexion()
                conexion.miCursor.execute("SELECT * FROM MONOPATIN where fechaUltimoPrecio BETWEEN '{}' AND '{}' ".format(fecha_cero, fecha_usuario))
                datos = conexion.miCursor.fetchall()
                for i in datos:
                    print(i)

            if nro == 0:
                break
            if nro == 8:
                ProgramaPrincipal.crearTablas(self)
            if nro == 9:
                ProgramaPrincipal.borrarTablas(self)

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("CREATE TABLE MONOPATIN (_id INTEGER PRIMARY KEY , modelo VARCHAR(30), marca  VARCHAR(30), potencia VARCHAR(30), precio REAL, color VARCHAR(30), cantidadDisponibles INTEGER, fechaUltimoPrecio DATETIME)")
        conexion.miCursor.execute("CREATE TABLE HISTORICA (_id INTEGER PRIMARY KEY , modelo VARCHAR(30), marca  VARCHAR(30), potencia VARCHAR(30), precio REAL, color VARCHAR(30), cantidadDisponibles INTEGER, fechaUltimoPrecio DATETIME)")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def borrarTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATIN")
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICA")
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

class monopatin:
    def __init__(self, modelo, marca, potencia, precio, color, cantidadDisponibles, fechaUltimoPrecio:date):
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia
        self.precio = precio
        self.color = color
        self.cantidadDisponibles = cantidadDisponibles
        self.fechaUltimoPrecio = fechaUltimoPrecio

    def cargar_monopatin(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MONOPATIN (modelo, marca, potencia, precio, color, cantidadDisponibles, fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(self.modelo,self.marca,self.potencia,self.precio,self.color,self.cantidadDisponibles,self.fechaUltimoPrecio))
            conexion.miCursor.execute("INSERT INTO HISTORICA (modelo, marca, potencia, precio, color, cantidadDisponibles, fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(self.modelo,self.marca,self.potencia,self.precio,self.color,self.cantidadDisponibles,self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un Monopatin")
        finally:
            conexion.cerrarConexion()

    def modificar_monopatin(self, marca, precio):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MONOPATIN SET precio='{}' where marca='{}'".format(precio, marca))
            conexion.miConexion.commit()
            print("Monopatin modificado correctamente")
        except:
            print('Error al actualizar un monopatin')
        finally:
            conexion.cerrarConexion()  

    def borrar_monopatin(self, marca):
        conexion=Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DELETE FROM MONOPATIN where marca= '{}' ".format(marca))
        conexion.miConexion.commit()

    def mostrar(self):
        conexion=Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("SELECT * FROM MONOPATIN")
        datos = conexion.miCursor.fetchall()
        for i in datos:
            print(i)

    def cargar_stock(self, marca):
        conexion=Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("UPDATE MONOPATIN SET cantidadDisponibles=cantidadDisponibles+1 where marca='{}'".format(marca))
        conexion.miConexion.commit()

class Conexiones:

    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria-MONO")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()     

programa = ProgramaPrincipal()
programa.menu()