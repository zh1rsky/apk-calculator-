from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

BUTTONS = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", ".", "+",
]


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.display = Label(text="0", font_size=60, size_hint_y=0.25,
                             halign="right", valign="middle")
        self.display.bind(size=lambda w, s: setattr(w, "text_size", s))
        self.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=5, padding=5)
        for b in BUTTONS:
            grid.add_widget(Button(text=b, font_size=36,
                                   on_press=self.on_button))
        grid.add_widget(Button(text="=", font_size=36, on_press=self.calculate))
        self.add_widget(grid)

    def on_button(self, btn):
        if btn.text == "C":
            self.display.text = "0"
        elif self.display.text in ("0", "Ошибка"):
            self.display.text = btn.text
        else:
            self.display.text += btn.text

    def calculate(self, _):
        try:
            result = eval(self.display.text, {"__builtins__": {}})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display.text = str(result)
        except Exception:
            self.display.text = "Ошибка"


class CalcApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalcApp().run()
