#formato usuario = {"nombre":"", "username":"", "password":"","estado":""}
usuarios = []
tickets = []
import time
import os
#Agregar una nueva clase pertinente a la aplicación que están desarrollando e 
class Superadmin():
    def __init__(self, nivel, nombre, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc
        #identificar en ella al menos cuatro atributos (uno de ellos debe ser opcional). 
        self.permisos = ["crear_usuarios", "crear_grupo", "crear_rol", "crear_permiso", "eliminar_usuario"]
    def asignar_permisos():
         pass
    
    def cambiar_nivel(self, usuario, nivel):
         for user in usuarios:
            if user["username"] == usuario:
                    user["nivel"] = nivel
                    print("Nivel cambiado")
                    return
         print("Usuario no encontrado")
    
    def eliminar_usuario(self, usuario):
         for user in usuarios:
            if user["username"] == usuario:
                    user["estado"] = "eliminado"
                    print("Usuario eliminado")
                    return
         print("Usuario no encontrado")

class Admin():
    def __init__(self, nivel, nombre, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc
        self.permisos = ["crear_usuarios", "crear_grupo", "suspender_usuario"]
    def mostrar_datos(self):
        print(f"Hola, mis datos son:\n{self.nombre}\n{self.desc}\n")

    def crear_usuario(self, username, password, nombre, **kwargs):
            print("creando nuevo usuario ...")
            usuario_nuevo = {"nombre":nombre, "username": username, "password": password, "estado":"creado", "nivel":0}
            #formato usuario = {"nombre":"", "username":"", "password":"","estado":""}
            usuarios.append(usuario_nuevo)
            print(f"he creado el usuario {username}")
            for usuario in usuarios: print(usuario)

    def suspender_usuario(self, usuario):
        for user in usuarios:
            if user["username"] == usuario:
                    user["estado"] = "suspendido"
                    print("Usuario suspendido")
                    return
        print("Usuario no encontrado")

class Regular():
    def __init__(self, nivel, nombre, username, password, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc
        self.username = username
        self.password = password
        self.estado = "creado"


    def logout(self):
        self.estado = "offline"

    def login(self, username, password):
        for user in usuarios:
            if user["username"] == username:
                if user["password"] == password:
                    self.estado = "logueado"
                    print(f"Bienvenido {user['username']}")
                    return
        print("Usuario o password incorrectos")
        
    def pedir_soporte(self, comentario):
        print("Ha pedido soporte exitosamente, por favor, espere...")
        #time.sleep(9999)
        tickets.append({"nombre":self.nombre, "comentario":comentario})
 
#version inventada de sobrecarga
#   def mis_profesores(self, profesor_1= None, profesor_2=None):
#             if profesor_1 != None and profesor_2 != None:
#               print("Tiene dos docentes, {profesor_1} y {profesor_2}")
#              elif profesor_1 != None or profesor_2 != None:
#                if profesor_1 == None: print("Tiene un docente, {profesor_1}")
#                if profesor_2 == None: print("Tiene un docente, {profesor_2}")
#              else:
#                  print("No hay niun profesor")
#sobrecarga flexible con *args -> atrapar todos los argumentos en una tupla que puede revisar el metodo.

    def mis_profesores(self, *args):
        if len(args) >2:
            print(f"Tiene {len(args)} docentes")
        if len(args) == 2:
            print(f"Tiene dos docentes, {args[0]} y {args[1]}")
        elif len(args) == 1:
            print(f"Tiene un docente, {args[0]}")
        else:
            print("No hay ningún profesor")
"""
class sumClass:
    def sum(self, a = None, b = None, c = None):
        if a != None and b == None or c == None:
            print("Provide more numbers") #if there is only 1 number as input
        else:   
            print("First method:", a + b + c) #for calculating the sum
        
obj=sumClass()
obj.sum(19, 8, 77)#104
obj.sum(18)#Provide more numbers
"""
class Invitado():
    def __init__(self, nivel, nombre, desc):
        self.nivel = "usuario invitado"
        self.nombre = nombre
        self.desc = "Cuenta de usuario invitado"
        
    def consultar_clase(self):
        print(f"Soy de clase {str(self.__class__)}\n")
        
    def irse(self):
        print("Adios.png")
        os.close()
        
    def registrarse(self):
        administrador.crear_usuario(input("ingrese un usuario: "), input("ingrese una contraseña: "))
    def dejar_comentario(self):
        nombre = input("ingrese su nombre:")
        comentario = input("Ingrese su feedback:")
        tickets.append({"nombre":nombre, "comentario":comentario})

administrador = Admin(1, "admin", "cuenta administrativa")       
usuario_basico = Regular(2, "usuario_regular1", "username1", "1234", "cuenta regular")
usuario_invitado = Invitado(3, "invitado", "cuenta invitado")
superadmini = Superadmin(0, "Renato", "Cuenta de supervision")
#administrador.crear_usuario("username1", "1234")


usuario_basico.login("username1", "1234")
#if else typeerror <-----------------
#usuario_basico.pedir_soporte()
usuario_basico.mis_profesores("antonio", "pancho")
administrador.crear_usuario("pepitoMAX","1234","pepito")
administrador.suspender_usuario("pepitoMAX")
superadmini.cambiar_nivel("pepitoMAX", 2)
usuario_basico.pedir_soporte("auxilio")
print(f"tickets:\n{tickets}")
print(f"usuarios:\n{usuarios}")
"""
DESARROLLO - Continuación del trabajo.
-HACERLO EN GITHUB PUBLICO
-Agréguela al diagrama intuitivo que realizó en la actividad anterior.
- Se deberá crear métodos para cada uno de los usuarios. Piensen en diferentes acciones particulares
que pueda ejecutar cada una de sus clases. 
Desarrolle cuatro métodos por cada clase.
Dos deben incluir acciones que afecten números y dos que afecten strings. !!!!!!!!!
-Al menos uno de estos métodos debe aplicar los contenidos de ‘sobrecarga de métodos’.
-También se solicita que existan condiciones para realizar las validaciones correspondientes.

El entregable es un script .PY
- El tiempo máximo para resolver la evaluación es el periodo correspondiente a una clase regular.

"""