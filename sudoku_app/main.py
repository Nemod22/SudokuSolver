import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.camera import Camera #poorly behaves on android
from camera4kivy import Preview
from kivy.utils import platform
import os
from sudoku_image_recognition import solve_from_image_and_display



class Sudoku(App):

    def on_start(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            from jnius import autoclass
            request_permissions([
            Permission.CAMERA,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE])

            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            ActivityInfo = autoclass("android.content.pm.ActivityInfo")
            activity = PythonActivity.mActivity
            # set orientation according to user's preference
            activity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_USER)

            from camera4kivy.preview_camerax import PreviewCameraX  
            #method/monkey patching where  the image gets saved
            def capture_photo(self, location = '',  subdir = '', name = ''):
                if self._camera:
                    self.capture_in_progress = True
                    self._camera.capture_photo(subdir, name, True)
            
            PreviewCameraX.capture_photo = capture_photo

    def on_stop(self):
        self.preview.disconnect_camera()
  
        
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.preview = Preview()
        self.preview.connect_camera(enable_analyze_pixels = True)
        self.layout.add_widget(self.preview)
        self.take_photo_button = Button(text="Take Photo")
        self.take_photo_button.bind(on_press=self.take_photo)
        self.layout.add_widget(self.take_photo_button)

        return self.layout

    def take_photo(self, *args):
        if platform == 'android':
            from android.storage import app_storage_path
            self.preview.capture_photo(location='', subdir = 'picture_temp', name = 'photo.jpg')
        else:
            self.preview.capture_photo(location='picture_temp', subdir = '.', name = 'photo')
            
        solve_from_image_and_display(os.path.join(os.getcwd(), 'picture_temp/photo.jpg'), os.path.join(os.getcwd(), 'picture_temp/solved.jpg'))
        self.image = Image(source=os.path.join(os.getcwd(), 'picture_temp/solved.jpg'), nocache=True)
        self.layout.clear_widgets()
        self.layout.add_widget(self.image)

        self.retake_photo_button = Button(text="Retake Photo")
        self.retake_photo_button.bind(on_press=self.retake_photo)
        self.layout.add_widget(self.retake_photo_button)

    def retake_photo(self, *args):
        self.layout.clear_widgets()
        self.layout.add_widget(self.preview)

        self.take_photo_button = Button(text="Take Photo")
        self.take_photo_button.bind(on_press=self.take_photo)
        self.layout.add_widget(self.take_photo_button)
    

if __name__ == '__main__':
    Sudoku().run()