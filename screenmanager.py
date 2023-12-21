from kivy.uix.screenmanager import ScreenManager, Screen
import sympy as sp
from kivy.properties import StringProperty
import re

class FirstPage(Screen):
    expression = StringProperty()

    def add_to_expression(self, value):
        self.expression += str(value)

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            expr = self.expression

            # Replace text with sympy trigonometric functions
            expr = expr.replace('sin', 'sp.sin')
            expr = expr.replace('cos', 'sp.cos')
            expr = expr.replace('tan', 'sp.tan')
            expr = expr.replace('asin', 'sp.asin')
            expr = expr.replace('acos', 'sp.acos')
            expr = expr.replace('atan', 'sp.atan')

            # Handle exponent (^)
            expr = expr.replace('^', '**')

            expr = expr.replace('pi', 'sp.pi')

            expr = expr.replace('sqrt', 'sp.sqrt')
            expr = expr.replace('root', 'sp.root')
            expr = expr.replace('log', 'sp.log')
            
            x = sp.symbols('x')
            result = eval(expr, {"sp": sp, "x": x})
            
            # If the result is a sympy object, convert it to a float
            if isinstance(result, sp.Basic):
                result = float(result.evalf())

            self.expression = str(result)
        except Exception as e:
            print(e)
            self.expression = "Error"

class MainScreenManager(ScreenManager):
    pass
