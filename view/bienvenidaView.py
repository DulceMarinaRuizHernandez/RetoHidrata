import flet as ft

class BienvenidaView(ft.Column):
    def __init__(self, controlador):
        super().__init__()
        # Guardamos una referencia al controlador que nos pasan desde afuera
        self.controlador = controlador
        
        # 1. Creamos los componentes (Widgets)
        self.texto_bienvenida = ft.Text(
            "¡Bienvenidos a nuestra App de POO de segundo A de ciencia de datos e informacion!", 
            size=30, 
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_800
        )
        
        self.boton_inicio = ft.Button(
            content="Ir al Menú de Opciones",
            icon=ft.Icons.PLAY_ARROW,
            # Aquí le decimos al botón: "Cuando te toquen, avísale al controlador"
            on_click=self.controlador.ir_al_menu 
        )

        # 2. Configuramos la alineación de la columna
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.CENTER
        
        # 3. Agregamos los componentes a la vista (la columna)
        self.controls = [
            self.texto_bienvenida,
            ft.Divider(height=20, color="transparent"), # Un pequeño espacio
            self.boton_inicio
            
        ]