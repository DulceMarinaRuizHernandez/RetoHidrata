import flet as ft

class OperacionesMathView(ft.View):
    def __init__(self, controlador):
        # Creamos la lista de opciones
        self.lista_operaciones = ft.Dropdown(
            label="Selecciona una operación",
            options=[
                ft.dropdown.Option("Suma"),
                ft.dropdown.Option("Resta"),
                ft.dropdown.Option("Multiplicación"),
                ft.dropdown.Option("División"),
            ],
            width=300,
        )
        
        # Campos para los números
        self.num1 = ft.TextField(label="Número 1", value="0")
        self.num2 = ft.TextField(label="Número 2", value="0")
        self.resultado = ft.Text("Resultado: ", size=20)

        super().__init__(
            route="/operaciones",
            controls=[
                ft.Text("Calculadora Científica", size=30),
                self.num1,
                self.num2,
                self.lista_operaciones,
                ft.ElevatedButton("Calcular", on_click=controlador.ejecutar_calculo),
                self.resultado
            ]
        )

