import os
import time

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("\n\t Presiona Enter para continuar...")
