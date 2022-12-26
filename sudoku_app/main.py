import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.utils import platform
import os
from sudoku_image_recognition import solve_from_image_and_display

class Sudoku(App):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([
            Permission.CAMERA,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE])
        self.layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        self.layout.add_widget(self.camera)

        self.take_photo_button = Button(text="Take Photo")
        self.take_photo_button.bind(on_press=self.take_photo)
        self.layout.add_widget(self.take_photo_button)

        return self.layout

    def take_photo(self, *args):
        self.camera.export_to_png((os.path.join(os.getcwd(), 'sudoku_app/photo.png')))
        solve_from_image_and_display(os.path.join(os.getcwd(), 'sudoku_app/photo.png'), os.path.join(os.getcwd(), 'sudoku_app/solved.png'))
        self.image = Image(source=os.path.join(os.getcwd(), 'sudoku_app/solved.png'), nocache=True)
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
    Sudoku().run()
