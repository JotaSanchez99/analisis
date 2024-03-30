from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import json


class InventoryMenu(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inventory = self.load_inventory()  # Cargar elementos de inventario desde un archivo

    def build(self):
        # Diseño de la aplicación: un diseño vertical que contiene una lista de elementos y botones para agregar, eliminar y modificar elementos
        layout = BoxLayout(orientation='vertical')

        # Etiqueta para mostrar la lista de elementos del inventario
        self.inventory_label = Label(text="Inventario:")
        layout.add_widget(self.inventory_label)

        # Botones para agregar, eliminar y modificar elementos
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        
        add_button = Button(text="Agregar", size_hint=(0.3, 1), background_color=(0.2, 0.6, 0.8, 1))
        add_button.bind(on_press=self.add_item)
        
        remove_button = Button(text="Eliminar", size_hint=(0.3, 1), background_color=(0.8, 0.2, 0.2, 1))
        remove_button.bind(on_press=self.remove_item)
        
        modify_button = Button(text="Modificar", size_hint=(0.3, 1), background_color=(0.2, 0.8, 0.2, 1))
        modify_button.bind(on_press=self.modify_item)
        
        buttons_layout.add_widget(add_button)
        buttons_layout.add_widget(remove_button)
        buttons_layout.add_widget(modify_button)

        layout.add_widget(buttons_layout)

        self.update_inventory_label()  # Actualizar la etiqueta de inventario al iniciar la aplicación

        return layout

    def add_item(self, instance):
        # Función para agregar un nuevo elemento al inventario
        text_input = TextInput(hint_text="Nuevo elemento")
        text_input.bind(on_text_validate=self.save_item)
        self.root.add_widget(text_input)

    def save_item(self, instance):
        # Función para guardar un nuevo elemento en el inventario
        item_name = instance.text
        if item_name:
            self.inventory.append(item_name)
            self.update_inventory_label()
            self.save_inventory()  # Guardar los cambios en el inventario en el archivo
            self.root.remove_widget(instance)

    def remove_item(self, instance):
        # Función para eliminar el último elemento del inventario
        if self.inventory:
            removed_item = self.inventory.pop()
            self.update_inventory_label()
            self.save_inventory()  # Guardar los cambios en el inventario en el archivo

    def modify_item(self, instance):
        # Función para modificar el último elemento del inventario
        if self.inventory:
            modified_item = self.inventory[-1] + " (modificado)"
            self.inventory[-1] = modified_item
            self.update_inventory_label()
            self.save_inventory()  # Guardar los cambios en el inventario en el archivo

    def update_inventory_label(self):
        # Actualiza la etiqueta de inventario para mostrar la lista de elementos
        inventory_text = "\n".join(self.inventory)
        self.inventory_label.text = "Inventario:\n" + inventory_text

    def save_inventory(self):
        # Guardar los elementos del inventario en un archivo JSON
        with open("inventory.json", "w") as file:
            json.dump(self.inventory, file)

    def load_inventory(self):
        # Cargar los elementos del inventario desde un archivo JSON
        try:
            with open("inventory.json", "r") as file:
                inventory = json.load(file)
        except FileNotFoundError:
            inventory = []
        return inventory


if __name__ == '__main__':
    InventoryMenu().run()

