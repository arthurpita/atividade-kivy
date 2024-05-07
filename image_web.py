from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage(source='https://s2-gshow.glbimg.com/aADB5L1u9RzF_qwqoJ2bnDsI2Zw=/0x0:3855x5782/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/I/4/dvg659QKaM5AGNhQxdlQ/davi-bbb-24.jpg')
    
if __name__ == '__main__':
    MinhaApp().run()