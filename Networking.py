# Para ello se debe crear una clase NetworkElement que almacene en su estado: 
# el tipo de dispositivo (router, switch, firewall, etc.), el nombre, su IP de management, 
# el fabricante y el modelo.

# Tambien se desea crear una subclase llamada Router, otra Switch y otra Firewall, 
# que al instanciarse, no solicite que se indique el tipo de dispositivo, 
# sino que lo agregue automaticámente.

# Sin implementar, defina funciones para hacer ping, 
# conectarse y desconectarse por ssh/telnet, y ejecutar commandos.

import paramiko



class NetworkElement:

   
    def __init__(self):
        
        self.ip = '0.0.0.0'
        self.nombre = 'NA'
        self.fabricante = 'NA'
        self.modelo = 'NA'
        self.tipo = 'NetworkElement'
        
    def ping(self):
        pass
    
    def conectar_ssh(self):
        pass
    
    def desconectar_ssh(self):
        pass
        
    def ejecutar_comando(self, comando):
        pass
    
    
class Router(NetworkElement):
    
     def __init__(self):
        
        # invoca al inicializador de la clase base (o clase super que es lo mismo) de la cual hereda
        super(Router, self).__init__()
        
        self.tipo = 'Router'
        
            
class Switch(NetworkElement):
    
     def __init__(self):
        
        # invoca al inicializador de la clase base (o clase super que es lo mismo) de la cual hereda
        super(Switch, self).__init__()
        
        self.tipo = 'Switch'
        
class Firewall(NetworkElement):
    
     def __init__(self):
        
        # invoca al inicializador de la clase base (o clase super que es lo mismo) de la cual hereda
        super(Firewall, self).__init__()
        
        self.tipo = 'Firewall'

class BaseDeDatos:
    
    def __init__(self):
        
        self.db = 'db_network_elements.db'
    
    def leer_todo(self):
        #abrir y leer el contenido de self.db y devolverlo
        with open(self.db, 'r') as db_file:
            print(db_file.read())
    
    def escribir_ne(self, ne):
        #agrega a self.db el nuevo elemento de red
        with open(self.db, 'a') as db_file:
            str_ne = {'nombre': ne.nombre, 'tipo': ne.tipo, 'ip': ne.ip, 'modelo': ne.modelo, 'fabricante': ne.fabricante }
            db_file.write(str(str_ne) + '\n')


class MenuPrincipal:
    
    def mostrar_menu_principal(self):
        #se debe preguntar si quiere agregar o listar
        #si selecciona agregar, llama a mostrar_formulario_ne
        #luego vuelve al menu principal
        #si selecciona listar debe llamar a mostrar_contenido_db
        while True:
            accion = input("Ingresa L si quieres listar los elementos de red.\nIngresa I si deseas agregar uno nuevo.\nIngresa S si deseas salir.\n\n")
            if accion.upper() == 'L':
                self.mostrar_contenido_db()
            if accion.upper() == 'I':
                self.mostrar_formulario_ne()
            if accion.upper() == 'S':
                break
    
    def mostrar_formulario_ne(self):
        #debe preguntar por los datos del elemento de red
        #al completar la carga, debe generar la instancia del elemento de red que corresponda
        #y guardarlo en la base de datos
        tipo = input("Ingresa R para Router, S para Switch o F para Firewall\n")
        
        if tipo.upper() == 'R':
            ne = Router()
        elif tipo.upper() == 'S':
            ne = Switch()
        elif tipo.upper() == 'F':
            ne = Firewall()
        else:
            print ('Ingreso cancelado por datos incorrectos.\n')
            return
            
        ne.ip = input('Ingrese la direccion IP:\n') 
        ne.nombre =  input('Ingrese el nombre:\n')
        ne.fabricante =  input('Ingrese el fabricante:\n')
        ne.modelo =  input('Ingrese el modelo:\n')
        
        db = BaseDeDatos()
        db.escribir_ne(ne)
          
    def mostrar_contenido_db(self):
        #debe mostrar el contenido de la base de datos
        db = BaseDeDatos()
        db.leer_todo()
    
#test de la aplicacion
m = MenuPrincipal()
m.mostrar_menu_principal()