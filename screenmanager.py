from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import sympy as sp
import time
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty

class FirstPage(Screen):
    expression = StringProperty()

    def add_to_expression(self, value):
        self.expression += str(value)

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
        except Exception:
            self.expression = "Error"

class MainScreenManager(ScreenManager):
    pass
