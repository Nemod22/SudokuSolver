import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera

class CameraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        self.layout.add_widget(self.camera)

        self.take_photo_button = Button(text="Take Photo")
        self.take_photo_button.bind(on_press=self.take_photo)
        self.layout.add_widget(self.take_photo_button)

        return self.layout

    def take_photo(self, *args):
        self.camera.export_to_png("sudoku_app/photo.png")
        self.image = Image(source="photo.png", nocache=True)
        self.layout.clear_widgets()
        self.layout.add_widget(self.image)

        self.retake_photo_button = Button(text="Retake Photo")
        self.retake_photo_button.bind(on_press=self.retake_photo)
        self.layout.add_widget(self.retake_photo_button)

    def retake_photo(self, *args):
        self.layout.clear_widgets()
        self.layout.add_widget(self.camera)

        self.take_photo_button = Button(text="Take Photo")
        self.take_photo_button.bind(on_press=self.take_photo)
        self.layout.add_widget(self.take_photo_button)

if __name__ == '__main__':
    CameraApp().run()
