from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

import wikipedia
import requests
import os

from wikipedia import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    
    def search_image(self):
        # Get User query
        query = self.manager.current_screen.ids.user_query.text
        print("QUERY: " + query)

        # Get wikipedia page and list of image urls
        try:
            page = wikipedia.page(query)
            image_link = page.images[0]

            print("IMAGE PATH: " + image_link)

            # Download Image
            image_path = "files/image.jpg"
            req = requests.get(image_link, headers=headers, stream=True)
            if req.status_code == 200:
                with open(image_path, 'wb') as f:
                    f.write(req.content)
            else:
                print('Error getting image')

        except Exception:
            image_path="files/gear5.jpeg"

        # Set image in the widget
        self.manager.current_screen.ids.img.source=image_path
        

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()
    
MainApp().run()