import os
import sys
if hasattr(sys, '_MEIPASS'):
    os.environ['KIVY_NO_CONSOLELOG'] = '1'
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
# from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, ILeftBodyTouch
from kivy.properties import StringProperty
from kivymd.uix.chip import MDChip
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine



from kivy.uix.boxlayout import BoxLayout



#---------------------CUSTOM ELEMENTS-----------------------#

class CustomPill(IRightBodyTouch, MDChip):
    pass

class ListItemWithChip(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("arm-flex")

    def __init__(self, **kwargs):
        super(ListItemWithChip, self).__init__(**kwargs)
        if self.text == 'Tasks':
            self.icon = StringProperty('arm-flex')
        elif self.text == 'Exercises':
            self.icon = StringProperty('arm-flex-outline')
        elif self.text == 'Streaks':
            self.icon = StringProperty('arm-flex')

    def get_icon(self):
        return self.icon

class InvalidLoginPopup(BoxLayout):
    """Opens dialog box when user enters invalid details when signing up or registering"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UsernameAlreadyExists(BoxLayout):
    """Opens dialog box when the user enter username that already exists"""


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item'''

    def __init__(self, pk=None, userid=None, **kwargs):
        super().__init__(**kwargs)
        # self.ids.check.active = check
        self.pk = pk
        self.userid = userid


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''


class CustomExpansionPanel(MDBoxLayout):
    ''''''

#-------------------------------------------------------------#



#-------------------Screens-------------------------------#

class LoginScreen(MDScreen):
    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text
        if self.ids.keepmeloggedin.active == True:
            keep_me_logged = True
        else:
            keep_me_logged = False


        if email != '' and password != '':

            self.invalid_popup()
        
        else:
            self.invalid_popup()


    def invalid_popup(self):
        '''Pop up for invalid entries'''
        self.dialog = MDDialog(
                type="custom",
                content_cls= InvalidLoginPopup(),
                size_hint=(.4, .4),
                auto_dismiss=True,
            )

        self.dialog.open()



class RecoverPasswordScreen(MDScreen):

    def invalid_popup(self):
        '''Pop up for invalid entries'''
        self.dialog = MDDialog(
                type="custom",
                content_cls= InvalidLoginPopup(),
                size_hint=(.4, .4),
                auto_dismiss=True,
            )

        self.dialog.open()


class ScreenManagement(ScreenManager):
    pass


#--------------------------------------------------------------------#



#-----------------------------MAIN APPLICATION------------------------#

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.accent_palette = 'Lime'
        self.theme_cls.theme_style = "Dark"

    def switch_window(self, window, boolean_val):
        if boolean_val == True:
            self.root.current = window
            self.root.transition.direction = "down"

        else:
            pass



MainApp().run()