import sys
import traceback
import os
import builtins
import math
import random
@author OVANDO CUPUL JOSE DOMINGO

class RestrictedEnvironment:
    def __init__(self):
        # Limitar todas las funcionaliades que se ingresan en el script
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

        self.safe_builtins['open'] = self.restricted_open

        self.safe_modules = {
            'math': math,
            'random': random,
        }

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
            user_code = input(">>> ")

            if user_code.lower() == 'exit':
                break

            result = environment.execute_code(user_code)
            print(result)
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
