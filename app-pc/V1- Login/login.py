from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
#from firebase_admin import firestore



# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('usuarios')  # create collection

#Creacion de la APP
class MainApp(MDApp):

    #Base de la app
    def build(self):
        #Configuracion visual inicial
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        #Creacion de la pantalla con el archivo .kv externo
        return Builder.load_file('login.kv')

    #Funcion para iniciar sesión
    def logger(self):
        
        #Datos de Login
        usuario = self.root.ids.user.text
        contraseña = self.root.ids.password.text
        
        #Codigo de legado - testear
        if contraseña == "12345":
            self.root.ids.welcome_label.text = f'Bienvenido {usuario}!'
        else:
            self.root.ids.welcome_label.text = "Error de contraseña"
            

    #Funcion para recuperar cuenta
    def recuperar(self):
        self.root.ids.welcome_label.text = "Bienvenido"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""


MainApp().run()