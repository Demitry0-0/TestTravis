from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from multiprocessing import Process

import qrcode

import qrserver


class MainApp(App):
    filename = "site.png"
    data = "data"
    textexit = "Выход"
    isConnected = False

    def build(self):
        self.main_layout = BoxLayout(orientation="vertical",
                                     padding=(0, 10, 0, 20),
                                     size_hint=(1, 0.25)
                                     )

        self.button = Button(text='Создать QR' if self.isConnected else "НЕТ ПОДКЛЮЧЕНИЯ",
                             size_hint=(.25, .5),
                             pos_hint={'center_x': .5, 'center_y': .25})

        self.button.bind(on_release=self.on_release_button)

        self.main_layout.add_widget(self.button)

        return self.main_layout

    def on_release_button(self, instance):
        if self.button.text == self.textexit or not self.isConnected:
            self.stop()

        qrcode.make(self.data).save(self.filename)

        self.img = Image(source=self.filename,
                         size_hint=(2.5, 2.5),
                         pos_hint={'center_x': .5, 'center_y': .5})
        self.main_layout.size_hint = (1, 1)
        self.main_layout.add_widget(self.img, 1)

        self.button.text = self.textexit


if __name__ == '__main__':
    app = MainApp()
    server = Process(target=qrserver.run)
    try:
        server.start()
        app.data = qrserver.url()
        app.isConnected = True
    except Exception:
        app.isConnected = False

    app.run()
    if server.is_alive():
        server.terminate()
