# File created by Utkarsh Gupta
# Dated 20/02/2020

# Touched on 20/02/2020 by Utkarsh Gupta

# GUI design of main screen

# Libraries
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label

import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import warnings
import SpeechAndTextProcessing as sp
from GenderDetection import genderDetectionOpenCV as gd
import symptomList

from reportsAnalyserScreen import reportsAnalyserScreenApp

# Layout inside the window
class mainScreenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(mainScreenLayout, self).__init__(**kwargs)
        warnings.filterwarnings('ignore')
        self.gender = gd.video()
        if self.gender == "man":
            self.speak = sp.SpeechTextProcessing(0)
        else:
            self.speak = sp.SpeechTextProcessing(1)
        # user details
        self.name = None
        self.age = None
        self.symptoms = None
        self.disease = None
        self.medicine = None
        self.language = None
        self.start()

    def onSendButtonPress(self):
        chatArea = self.ids['ChatArea2']
        message = self.ids['message_box']
        if message.text == "":
            return
        label = Label(text=message.text, font_size='20dp')
        #a = message.text
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)
        message.text = ""
        chatArea = self.ids['ChatArea1']
        label = Label(text=" ", font_size='20dp')
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)


    def onBaymaxResponse(self, message):
        chatArea = self.ids['ChatArea1']
        label = Label(text=message, font_size='20dp')
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)
        chatArea = self.ids['ChatArea2']
        label = Label(text=" ", font_size='20dp')
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)

    def greetingEnglish(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak.textToSpeech("Good Morning!")
            self.onBaymaxResponse("Good Morning!")
        elif 12 <= hour < 17:
            self.speak.textToSpeech("Good Afternoon!")
            self.onBaymaxResponse("Good Afternoon!")
        else:
            self.speak.textToSpeech("Good Evening!")
            self.onBaymaxResponse("Good Evening!")

    def start(self):
        self.greetingEnglish()


# Actual window
class mainScreenApp(App):
    def build(self):
        self.title = "Baymax"
        self.icon = "./assets/icons/baymaxIcon.png"
        Window.fullscreen = 'auto'
        return mainScreenLayout()

    def onSpeakButtonPress(self):
        print("Speak")

    def onReportsAnalyserButtonPress(self):
        self.get_running_app().stop()
        reportsAnalyserScreenApp().run()
