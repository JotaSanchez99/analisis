from kivy.lang import Builder
from kivymd.app import MDApp
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Crea un nuevo documento en Firestore
db = firestore.client()
collection = db.collection('usuarios')  # create collection


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('crud.kv')

    def agregar(self):
        res = collection.document(self.root.ids.usuario.text).set({  # insert document
            'nombre': self.root.ids.nombre.text,
            'apellidos': self.root.ids.apellidos.text,
            'password': self.root.ids.password.text,
        })
        self.root.ids.usuario.text = ""
        self.root.ids.nombre.text = ""
        self.root.ids.apellidos.text = ""
        self.root.ids.password.text = ""
        print(res)

    def modificar(self):
        res = collection.document(self.root.ids.usuario.text).update({  # update document
            'nombre': self.root.ids.nombre.text,
            'apellidos': self.root.ids.apellidos.text,
            'password': self.root.ids.password.text,
        })
        self.root.ids.usuario.text = ""
        self.root.ids.nombre.text = ""
        self.root.ids.apellidos.text = ""
        self.root.ids.password.text = ""
        print(res)

    def consultar(self):
        res = collection.document(self.root.ids.usuario.text).get().to_dict()
        self.root.ids.nombre.text = res['nombre']
        self.root.ids.apellidos.text = res['apellidos']
        self.root.ids.password.text = res['password']

    def eliminar(self):
        res = collection.document(self.root.ids.usuario.text).delete()  # delete document
        self.root.ids.usuario.text = ""
        self.root.ids.nombre.text = ""
        self.root.ids.apellidos.text = ""
        self.root.ids.password.text = ""
        print(res)

MainApp().run()
