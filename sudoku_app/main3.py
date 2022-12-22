from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.app import App
from sudoku_image_recognition import solve_from_image_and_display


class CameraExample(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a camera object

        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (300, 300)  # Specify the resolution

        # Create a button for taking photograph

        self.camaraClick = Button(text="Take Photo")
        self.camaraClick.size_hint = (.5, .2)
        self.camaraClick.pos_hint = {'x': .25, 'y': .75}
        self.camaraClick.bind(on_press=self.onCameraClick)

        layout.add_widget(self.cameraObject)
        layout.add_widget(self.camaraClick)

        return layout

    def onCameraClick(self, *args):
        path = 'sudoku_app/camera.png'
        self.cameraObject.export_to_png(path)
        solve_from_image_and_display(path)

# Start the Camera App


if __name__ == '__main__':
    
    CameraExample().run()