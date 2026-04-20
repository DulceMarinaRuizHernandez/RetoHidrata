import flet as ft
from view.bienvenidaView import BienvenidaView
from view.menuView import MenuView

class MainController:
    def __init__(self, page: ft.Page):
        # El controlador guarda la referencia de la página principal
        self.page = page
        self.page.title = "App POO con MVC"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        
        # Al iniciar, mostramos la bienvenida
        self.mostrar_bienvenida()

    def mostrar_bienvenida(self):
        """Limpia la pantalla y carga la vista de Bienvenida"""
        self.page.controls.clear()
        
        # Creamos una instancia de la Vista y le pasamos 'self' (este controlador)
        vista = BienvenidaView(self)
        
        self.page.add(vista)
        self.page.update()

    def ir_al_menu(self, e):
        """Este es el método que ejecuta el botón de la vista"""
        print("Cambiando al menú...")
        self.page.controls.clear()
        
        # Creamos una instancia de la Vista del Menú y le pasamos 'self' (este controlador)
        vista = MenuView(self)
        
        self.page.add(vista)
        self.page.update()

    def ir_a_saludo(self, e):
        """Muestra la vista de Saludo"""
        print("Cambiando a Saludo...")
        self.page.controls.clear()
        self.page.add(ft.Text("¡Hola Mundo!", size=25))
        self.page.update()

    def ir_a_operaciones(self, e):
        """Muestra la vista de Operaciones Matemáticas"""
        print("Cambiando a Operaciones...")
        self.page.controls.clear()
        self.page.add(ft.Text("Operaciones Matemáticas", size=25))
        self.page.update()

    def ir_a_figuras(self, e):
        """Muestra la vista de Figuras Geométricas"""
        print("Cambiando a Figuras...")
        self.page.controls.clear()
        self.page.add(ft.Text("Figuras Geométricas", size=25))
        self.page.update()

    def ir_a_persona(self, e):
        """Muestra la vista de Persona"""
        print("Cambiando a Persona...")
        self.page.controls.clear()
        self.page.add(ft.Text("Persona", size=25))
        self.page.update()

        # Dentro de tu clase MainController
def ejecutar_calculo(self, e):
    # 1. Obtenemos los datos de la vista
    n1 = float(self.vista_actual.num1.value)
    n2 = float(self.vista_actual.num2.value)
    opcion = self.vista_actual.lista_operaciones.value

    # 2. Decidimos qué operación hacer
    if opcion == "Suma":
        res = self.modelo.sumar(n1, n2)
    elif opcion == "Resta":
        res = self.modelo.restar(n1, n2)
    elif opcion == "multiplicación":
        res = self.modelo.multiplicar(n1, n2)
    elif opcion == "División":
        res = self.modelo.dividir(n1, n2)
    elif opcion == "":
    # ... así con las demás ...

    # 3. Mostramos el resultado en la pantalla
        self.vista_actual.resultado.value = f"Resultado: {res}"
        self.page.update()