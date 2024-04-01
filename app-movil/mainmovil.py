from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import json
import os

class InventoryMenu(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inventory = self.load_inventory()

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

        self.update_inventory_label()

        return self.layout

    def update_inventory_label(self):
        if not self.inventory:
            self.inventory_label.text = "Inventario vacío"
        else:
            inventory_text = "\n".join([f'{item["nombre"]}: {item["stock"]}' for item in self.inventory])
            self.inventory_label.text = f"Inventario:\n{inventory_text}"

    def add_item_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        self.name_input = TextInput(hint_text='Nombre del producto')
        self.stock_input = TextInput(hint_text='Stock', input_filter='int')
        add_button = Button(text='Agregar')
        add_button.bind(on_press=self.add_item)
        
        content.add_widget(self.name_input)
        content.add_widget(self.stock_input)
        content.add_widget(add_button)
        
        self.popup = Popup(title="Agregar Producto", content=content, size_hint=(0.8, 0.5))
        self.popup.open()

    def add_item(self, instance):
        name = self.name_input.text
        stock = self.stock_input.text
        if name and stock.isdigit():
            self.inventory.append({"nombre": name, "stock": int(stock)})
            self.update_inventory_label()
            self.save_inventory()
            self.popup.dismiss()

    def remove_item_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        self.name_input = TextInput(hint_text='Nombre del producto a eliminar')
        remove_button = Button(text='Eliminar')
        remove_button.bind(on_press=self.remove_item)
        
        content.add_widget(self.name_input)
        content.add_widget(remove_button)
        
        self.popup = Popup(title="Eliminar Producto", content=content, size_hint=(0.8, 0.4))
        self.popup.open()

    def remove_item(self, instance):
        name = self.name_input.text
        self.inventory = [item for item in self.inventory if item["nombre"] != name]
        self.update_inventory_label()
        self.save_inventory()
        self.popup.dismiss()

    def modify_item_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        self.name_input = TextInput(hint_text='Nombre del producto a modificar')
        self.new_stock_input = TextInput(hint_text='Nuevo stock', input_filter='int')
        modify_button = Button(text='Modificar')
        modify_button.bind(on_press=self.modify_item)
        
        content.add_widget(self.name_input)
        content.add_widget(self.new_stock_input)
        content.add_widget(modify_button)
        
        self.popup = Popup(title="Modificar Producto", content=content, size_hint=(0.8, 0.5))
        self.popup.open()

    def modify_item(self, instance):
        name = self.name_input.text
        new_stock = self.new_stock_input.text
        for item in self.inventory:
            if item["nombre"] == name and new_stock.isdigit():
                item["stock"] = int(new_stock)
                break
        self.update_inventory_label()
        self.save_inventory()
        self.popup.dismiss()

    def show_highest_stock(self, instance):
        highest_stock = sorted(self.inventory, key=lambda x: x['stock'], reverse=True)[:5]
        highest_stock_text = "\n".join([f'{item["nombre"]}: {item["stock"]}' for item in highest_stock])
        popup = Popup(title='Productos con mayor stock',
                      content=Label(text=highest_stock_text),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def load_inventory(self):
        if os.path.exists("inventory.json"):
            with open("inventory.json", "r") as file:
                return json.load(file)
        return []

    def save_inventory(self):
        with open("inventory.json", "w") as file:
            json.dump(self.inventory, file)

if __name__ == '__main__':
    InventoryMenu().run()
