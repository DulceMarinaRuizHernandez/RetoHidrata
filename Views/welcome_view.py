import flet as ft

class WelcomeView:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        icono = ft.Icon(icon=ft.icons.Icons.WATER, color=ft.Colors.BLUE_400, size=100)
        titulo = ft.Text("¡Bienvenido a HydroBoost!", size=30, color=ft.Colors.BLUE_900)
        
        # Agregamos on_click para ir a la ruta /login
        boton = ft.ElevatedButton(
            content=ft.Text("Entrar", color=ft.Colors.WHITE), 
            bgcolor=ft.Colors.CYAN_700,
            # ACTUALIZADO AQUÍ:
            on_click=lambda e: self.page.go("/login")
        )
        

        columna_principal = ft.Column(
            controls=[icono, titulo, boton],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        return columna_principal