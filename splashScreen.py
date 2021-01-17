# File created by Utkarsh Gupta
# Dated 30/12/2020

# Touched on 30/12/2020 by Utkarsh Gupta

# GUI design of splash screen

# Libraries
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config


# Main Screen
from mainScreen import mainScreenApp


# Layout inside the window
class splashScreenLayout(FloatLayout):
    pass


# Actual window
class splashScreenApp(App):
    def build(self):
        self.title = "Baymax"
        self.icon = "./assets/icons/baymaxIcon.png"
        Config.set('graphics', 'width', '480')
        Config.set('graphics', 'height', '270')
        Config.set('graphics', 'resizable', False)
        Config.write()
        return splashScreenLayout()

    def switchToMainScreen(self):
        self.stop()
        mainScreenApp().run()
