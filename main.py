from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.screenmanager import MDScreenManager

class LoginScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    pass

class TelaPrincipal(MDScreen):
    pass

class Denuncia(MDScreen):
    pass

class Perfil(MDScreen):
    pass

class App(MDApp, App):
    def build(self):
        Window.size = (300, 600)
        Builder.load_file(('main.kv'))
        sm = MDScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(TelaPrincipal())
        sm.add_widget(Denuncia())
        sm.add_widget(Perfil())
        return sm

App().run()