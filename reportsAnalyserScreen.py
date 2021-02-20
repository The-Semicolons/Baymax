# File created by Utkarsh Gupta
# Dated 30/12/2020

# Touched on 30/12/2020 by Utkarsh Gupta

# GUI design of main screen

# Libraries
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


#from mainScreen import mainScreenApp


class reportsAnalyserScreenLayout(GridLayout):
    def onHomeButtonPress(self):
        self.stop()
        #mainScreenApp().run()

class reportsAnalyserScreenApp(App):
    def build(self):
        self.title = "Baymax"
        self.icon = "./assets/icons/baymaxIcon.png"
        Window.fullscreen = 'auto'
        return reportsAnalyserScreenLayout()