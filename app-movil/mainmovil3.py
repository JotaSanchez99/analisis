import firebase_admin
from firebase_admin import credentials, firestore
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from uuid import uuid4

# Inicializa Firebase Admin.
# la llave no esta  en doc porqe tenes el proyecto publico ... por obias razones no subire el doc llave mio ... xD
# confundi el id con el codigo vean como lo arreglan xD es oslo modicar una cosa UwU
#QUZAS   en el main 2 esta arrglo el tema la id hacer lo mismo aca .... 

cred = credentials.Certificate('')
firebase_admin.initialize_app(cred)
db = firestore.client()

class InventoryMenu(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.inventory_label = Label(size_hint=(1, 0.9))
        self.layout.add_widget(self.inventory_label)

        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        
        add_button = Button(text="Agregar")
        add_button.bind(on_press=self.add_item_popup)
        
        remove_button = Button(text="Eliminar")
        remove_button.bind(on_press=self.remove_item_popup)
        
        modify_button = Button(text="Modificar")
        modify_button.bind(on_press=self.modify_item_popup)
        
        highest_stock_button = Button(text="Mayor Stock")
        highest_stock_button.bind(on_press=self.show_highest_stock)
        
        buttons_layout.add_widget(add_button)
        buttons_layout.add_widget(remove_button)
        buttons_layout.add_widget(modify_button)
        buttons_layout.add_widget(highest_stock_button)
        
        self.layout.add_widget(buttons_layout)
        
        self.load_inventory()

        return self.layout

    def load_inventory(self):
        docs = db.collection('inventario').order_by('Cantidad', direction=firestore.Query.DESCENDING).get()
        inventory_text = "\n".join([f'{doc.to_dict()["Nombre"]} (ID: {doc.id}), Código: {doc.to_dict()["Codigo"]}, Precio: {doc.to_dict()["Precio"]}, Stock: {doc.to_dict()["Cantidad"]}' for doc in docs])
        self.inventory_label.text = f"Inventario:\n{inventory_text}"

    def add_item_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        
        self.name_input = TextInput(hint_text='Nombre del producto')
        self.code_input = TextInput(hint_text='Código del producto')
        self.price_input = TextInput(hint_text='Precio', input_filter='float')
        self.quantity_input = TextInput(hint_text='Cantidad en stock', input_filter='int')
        
        add_button = Button(text='Agregar')
        add_button.bind(on_press=self.add_item)
        
        content.add_widget(self.name_input)
        content.add_widget(self.code_input)
        content.add_widget(self.price_input)
        content.add_widget(self.quantity_input)
        content.add_widget(add_button)
        
        self.popup = Popup(title="Agregar Producto", content=content, size_hint=(0.8, 0.6))
        self.popup.open()

    def add_item(self, instance):
        product_data = {
            "Nombre": self.name_input.text,
            "Codigo": self.code_input.text,
            "Precio": float(self.price_input.text),
            "Cantidad": int(self.quantity_input.text)
        }
        db.collection('inventario').add(product_data)
        self.popup.dismiss()
        self.load_inventory()

    def remove_item_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        self.id_input = TextInput(hint_text='ID del producto a eliminar')
        remove_button = Button(text='Eliminar')
        remove_button.bind(on_press=self.remove_item)
        
        content.add_widget(self.id_input)
        content.add_widget(remove_button)
        
        self.popup = Popup(title="Eliminar Producto", content=content, size_hint=(0.8, 0.4))
        self.popup.open()

    def remove_item(self, instance):
        product_id = self.id_input.text
        db.collection('inventario').document(product_id).delete()
        self.popup.dismiss()
        self.load_inventory()

    def modify_item_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        self.id_input = TextInput(hint_text='ID del producto a modificar')
        self.new_quantity_input = TextInput(hint_text='Nueva cantidad en stock', input_filter='int')
        modify_button = Button(text='Modificar')
        modify_button.bind(on_press=self.modify_item)
        
        content.add_widget(self.id_input)
        content.add_widget(self.new_quantity_input)
        content.add_widget(modify_button)
        
        self.popup = Popup(title="Modificar Producto", content=content, size_hint=(0.8, 0.5))
        self.popup.open()

    def modify_item(self, instance):
        product_id = self.id_input.text
        new_quantity = int(self.new_quantity_input.text)
        db.collection('inventario').document(product_id).update({"Cantidad": new_quantity})
        self.popup.dismiss()
        self.load_inventory()

    def show_highest_stock(self, instance):
        # Esta función ya no es necesaria ya que load_inventory ya ordena por cantidad.
        # Pero si deseas limitar a los 5 primeros, podrías ajustar load_inventory o hacer una consulta específica aquí.
        # y me gusta com suena pero apreciaciones personales *( Yes, your Highness... CODE GEAS*(nombre del anime) )
        pass

if __name__ == '__main__':
    InventoryMenu().run()
