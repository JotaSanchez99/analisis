from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

# Cargar el archivo KV que define la interfaz de usuario
Builder.load_string(
    """
<RootWidget>:
    orientation: "vertical"

    MDButton:
        text: "Hello, KivyMD!"
        pos_hint: {"center_x": 0.5}
        on_release: app.button_click()
"""
)


class RootWidget(BoxLayout):
    pass


class MyApp(MDApp):
    def build(self):
        return RootWidget()

    def button_click(self):
        print("Button clicked!")


if __name__ == "__main__":
    MyApp().run()



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')

    def logger(self):
        usuario = self.root.ids.user.text
        contraseña = self.root.ids.password.text
        if contraseña == "12345":
            self.root.ids.welcome_label.text = f'Bienvenido {usuario}!'
        else:
            self.root.ids.welcome_label.text = "Error de contraseña"

    def recuperar(self):
        self.root.ids.welcome_label.text = "Bienvenido"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""


MainApp().run()
