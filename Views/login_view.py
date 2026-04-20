import flet as ft

class LoginView:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        titulo = ft.Text(value="Iniciar Sesión", size=30, color=ft.Colors.BLUE_900, weight=ft.FontWeight.BOLD)
        
        input_usuario = ft.TextField(label="Nombre de Usuario", border_color=ft.Colors.BLUE_400, prefix_icon=ft.icons.Icons.PERSON)
        input_password = ft.TextField(label="Contraseña", border_color=ft.Colors.BLUE_400, prefix_icon=ft.icons.Icons.LOCK, password=True, can_reveal_password=True)
        
        boton_ingresar = ft.ElevatedButton(content=ft.Text("Ingresar", color=ft.Colors.WHITE), bgcolor=ft.Colors.CYAN_700, width=200)
        
        boton_registro = ft.TextButton(
            content=ft.Text("¿No tienes cuenta? Regístrate aquí"),
            icon=ft.icons.Icons.APP_REGISTRATION,
            icon_color=ft.Colors.BLUE_600,
            # ACTUALIZADO AQUÍ:
            on_click=lambda e: self.page.go("/register")
        )

        columna_login = ft.Column(
            controls=[titulo, ft.Container(height=20), input_usuario, input_password, ft.Container(height=20), boton_ingresar, boton_registro],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=320 
        )
        
        return columna_login