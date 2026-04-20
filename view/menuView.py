import flet as ft
from view.operacionesMathView import OperacionesMathView


class MenuView(ft.Column):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        
        # Configuramos el título del menú
        self.titulo = ft.Text(
            "Menú de Opciones", 
            size=28, 
            weight=ft.FontWeight.BOLD
        )

        # Creamos los botones para cada sección
        # Cada botón llama a un método diferente en el controlador
        self.btn_saludo = ft.Button(
            content="Saludo 'Hola Mundo'", 
            icon=ft.Icons.WAVING_HAND,
            on_click=self.controlador.ir_a_saludo,
            width=300
        )
        
        self.btn_operaciones = ft.Button(
            content="Operaciones Matemáticas", 
            icon=ft.Icons.CALCULATE,
            on_click=self.controlador.ir_a_operaciones,
            width=300
        )
        
        self.btn_figuras = ft.Button(
            content="Perímetro y Área de Figuras", 
            icon=ft.Icons.SQUARE_FOOT,
            on_click=self.controlador.ir_a_figuras,
            width=300
        )

        self.btn_persona = ft.Button(
            content="Persona", 
            icon=ft.Icons.PERSON,
            on_click=self.controlador.ir_a_persona,
            width=300
        )


        self.btn_volver = ft.TextButton(
            "Volver a Bienvenida", 
            on_click=self.controlador.mostrar_bienvenida
        )

        # Centramos todo en la columna
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 15 # Espacio entre botones

        # Agregamos los controles a la vista
        self.controls = [
            self.titulo,
            ft.Divider(height=10, color="transparent"),
            self.btn_saludo,
            self.btn_operaciones,
            self.btn_figuras,
            self.btn_persona,
            ft.Divider(height=10),
            self.btn_volver
            
        ]