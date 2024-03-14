from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

import time
from filesharer import FileSharer
import webbrowser

Builder.load_file('frontend.kv')

class WebcamScreen(Screen):

    def start(self):
        """Starts the Camera"""
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'

    def stop(self):
        """Stops the Camera on the last frame"""
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'

    def capture(self):
        #Save Image using date and time
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath= f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)

        #Set screen to next screen
        #Manager goes to the parent -> root widget
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):
    
    def create_link(self):
        """Puts the image into the cloud and gets the link"""
        filepath = App.get_running_app().root.ids.webcam_screen.filepath
        fileSharer = FileSharer(filepath)
        self.url = fileSharer.share()

        #Put it on the label
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = "Create Link First"

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = "Create Link First"


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()
    
MainApp().run()