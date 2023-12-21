# screenmanager.py
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.toast import toast

class MainScreenManager(ScreenManager):
    pass

class FirstPage(Screen):
    expression = StringProperty("")  # User-entered expression
    result = StringProperty("")  # Result of the calculation

    def append(self, text):
        self.expression += text  # Append character to expression

    def clear(self):
        self.expression = ""  # Clear expression
        self.result = ""  # Clear result

    def calculate(self):
        try:
            self.result = str(eval(self.expression))  # Evaluate expression and set result
        except SyntaxError:
            toast("Invalid input")  # Show toast for syntax error
            self.clear()
        except ZeroDivisionError:
            toast("Cannot divide by zero")  # Show toast for division by zero
            self.clear()
        except Exception:
            toast("Something went wrong")  # Show toast for other errors
            self.clear()
