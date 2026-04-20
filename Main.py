import flet as ft
from controller.mainController import MainController

def main(page: ft.Page):
    MainController(page)
    

ft.app(target=main)