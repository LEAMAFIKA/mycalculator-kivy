from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (0.8, 0.8, 0.8, 1)
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.text_input = TextInput(font_size=40, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.text_input)

        buttons = [
            ['AC', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, font_size=24)

                if label in ('/', '*', '-', '+', '='):
                    button.background_color = (1.0, 0.5, 0.0, 1.0)  # Orange
                elif label in ('AC', '+/-', '%'):
                    button.background_color = (0.6, 0.6, 0.6, 1)  # Grid
                else:
                    button.background_color = (0.4, 0.4, 0.4, 1)  # Gris fonc

                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current_text = self.text_input.text
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(current_text))
                self.text_input.text = result
            except Exception as e:
                self.text_input.text = 'Error'
        elif button_text == 'AC':
            self.text_input.text = ''
        elif button_text == '+/-':
            if current_text and current_text[0] == '-':
                self.text_input.text = current_text[1:]
            else:
                self.text_input.text = '-' + current_text
        elif button_text == '%':
            try:
                result = str(eval(current_text) / 100)
                self.text_input.text = result
            except Exception as e:
                self.text_input.text = 'Error'
        else:
            if button_text in self.operators:
                if self.last_was_operator:
                    return
                elif not current_text or current_text[-1] in self.operators:
                    return
                else:
                    self.last_was_operator = True
            else:
                self.last_was_operator = False

            self.text_input.text += button_text


if __name__ == '__main__':
    Window.size = (230, 300)
    CalculatorApp().run()