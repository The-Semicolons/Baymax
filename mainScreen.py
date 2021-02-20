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
import TreeRunner as tr

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
        print(self.gender)
        #self.speak = sp.SpeechTextProcessing(1)
        # user details
        self.name = None
        self.age = None
        self.symptoms = None
        self.disease = None
        self.medicine = None
        self.language = None
        self.message = None
        self.data = list()
        self.index = 0
        self.questions = ["self.start1()", "self.start2()", "self.start3()", "self.predict()"]

    def onSendButtonPress(self):
        chatArea = self.ids['ChatArea2']
        message = self.ids['message_box']
        if message.text == "":
            return
        label = Label(text=message.text, font_size='20dp')
        self.data.append(message.text)
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)
        message.text = ""
        chatArea = self.ids['ChatArea1']
        label = Label(text=" ", font_size='20dp')
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)
        if self.index > 3:
            return
        else:
            exec(self.questions[self.index])
            self.index += 1


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

    def greetingHindi(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak.textToSpeech("Shubh Prabhaat")
            self.onBaymaxResponse("शुभ प्रभात")
        elif 12 <= hour < 17:
            self.speak.textToSpeech("namaskaar")
            self.onBaymaxResponse("नमस्कार")
        else:
            self.speak.textToSpeech("namaskaar")
            self.onBaymaxResponse("नमस्कार")

    def start(self):
        self.onBaymaxResponse("Please Select a Language: English/Hindi")
        self.onBaymaxResponse("कृपया एक भाषा चुनें:   अंग्रेजी / हिंदी")
        self.speak.textToSpeech("Please Select a Language: English/Hindi")
        self.speak.textToSpeech("Kripya eak Bhaashaaa Chunei: Angrezi yaa Hindi")

    def start1(self):
        self.speak.textToSpeech("Hello there!")
        self.onBaymaxResponse("Hello there!")
        self.speak.textToSpeech("I'm Baymax, Your Personal Health Assistant")
        self.onBaymaxResponse("I'm Baymax, Your Personal Health Assistant")
        self.speak.textToSpeech("I need some of your personal details to serve you better. So, Let's get started.")
        self.onBaymaxResponse("I need some of your personal details to serve you better. So, Let's get started.")
        self.speak.textToSpeech("What's your name?")
        self.onBaymaxResponse("What's your name?")

    def start2(self):
        self.speak.textToSpeech("What is your age")
        self.onBaymaxResponse("What is your age?")

    def start3(self):
        self.speak.textToSpeech("What are the symptoms that you are facing")
        self.onBaymaxResponse("What are the symptoms that you are facing...")

    def processData(self):
        print("process")
        self.symptoms = self.data[3].split(" ")
        patientSymptomsFinal = [i.lower() for i in self.symptoms]
        allSymptoms = symptomList.symptomList()
        symptomListForPrediction = []
        for i in range(131):
            symptomListForPrediction.append(0)
        for i in range(len(patientSymptomsFinal)):
            for j in range(131):
                if (patientSymptomsFinal[i] == allSymptoms[j]):
                    symptomListForPrediction[j] = 1

        return symptomListForPrediction

    def predict(self):
        print("predict")
        self.tree = tr.TreeRunner()
        self.disease = self.tree.predict(self.processData())
        self.speak.textToSpeech("Processing! please wait for few minutes...")
        self.onBaymaxResponse("Processing! please wait for few minutes...")
        self.speak.textToSpeech(("You might have " + str(self.disease)))
        self.onBaymaxResponse(("You might have " + str(self.disease)))


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
