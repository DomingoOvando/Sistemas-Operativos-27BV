import sys
import traceback
import os
import builtins
import math
import random

class RestrictedEnvironment:
    def __init__(self):
        # Limitar las funciones incorporadas
        self.safe_builtins = {
            'print': print,
            'input': input,
            'len': len,
            'str': str,
            'int': int,
            'float': float,
            'list': list,
            'tuple': tuple,
            'dict': dict,
            'range': range,
            'abs': abs,
            'sum': sum,
            'min': min,
            'max': max,
        }

        # Limitar el acceso al sistema de archivos
        self.safe_builtins['open'] = self.restricted_open

        # Limitar el acceso a algunos módulos
        self.safe_modules = {
            'math': math,
            'random': random,
        }

        # Variables globales disponibles para el usuario
        self.user_globals = {}

    def restricted_open(self, *args, **kwargs):
        raise RuntimeError("Función 'open' está deshabilitada en este entorno.")

    def execute_code(self, code):
        try:
            exec(code, {'__builtins__': self.safe_builtins}, self.user_globals)
        except Exception as e:
            return f"Error: {str(e)}"
        return "Evaluación exitosa."

def main():
    print("Bienvenido al jail de Python. Escribe 'exit' para salir.")
    environment = RestrictedEnvironment()

    while True:
        try:
            # Leer el código del usuario
            user_code = input(">>> ")

            # Salir si el usuario escribe 'exit'
            if user_code.lower() == 'exit':
                break

            # Ejecutar el código proporcionado por el usuario en el entorno restringido
            result = environment.execute_code(user_code)
            print(result)
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break
        except Exception as e:
            # Capturar excepciones para que no se interrumpa el programa principal
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
