import wikipedia
import requests

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        #Get wikipedia page and first image link
        page = wikipedia.page(query, 1)
        image_links = page.images[0]
        return image_links
    
    def download_image(self):
        # Download the image
        req = requests.get(self.get_image_link())
        filepath = 'files/image.jpg'
        with open(filepath, 'wb') as file:
            file.write(req.content)
        return filepath
    
    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()
        


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

