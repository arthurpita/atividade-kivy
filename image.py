from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source='/Users/Aluno.sesipaulista/Pictures/Screenshots/Captura de tela 2023-09-21 083412.png')
    
if __name__ == '__main__':
    MinhaApp().run()