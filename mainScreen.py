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
import pdfGenerator as pdfgen
import warnings
import SpeechAndTextProcessing as sp
from GenderDetection import genderDetectionOpenCV as gd
import plot as pt
import symptomList
import DiseaseToMedicine
import TreeRunner as tr
import exportToDatabase as database


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
        self.tree = tr.TreeRunner()
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
        self.pdf = None
        self.medication = None
        self.DB = None
        self.confidence = 0
        self.plt = pt.graph()
        self.questions = ["self.start1()", "self.start2()", "self.start3()", "self.predictDisease()",
                          "self.predictMedication()", "self.printPrescription()", "self.startExportingToDatabase()"]

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
        if self.index > 6:
            return
        else:
            exec(self.questions[self.index])
            self.index += 1

    def onBaymaxResponse(self, message, font="ARIAL"):
        chatArea = self.ids['ChatArea1']
        label = Label(text=message, font_size='20dp', font_name=font)
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)
        chatArea = self.ids['ChatArea2']
        label = Label(text=" ", font_size='20dp')
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)

    def onSpeakButtonPress(self):
        message = self.speak.speechToText()
        chatArea = self.ids['ChatArea2']
        label = Label(text=message, font_size='20dp')
        self.data.append(message)
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)
        chatArea = self.ids['ChatArea1']
        label = Label(text=" ", font_size='20dp')
        chatArea.bind(minimum_height=chatArea.setter('height'))
        chatArea.add_widget(label)
        self.ids['ChatAreaScrollView'].scroll_to(label)
        if self.index > 6:
            return
        else:
            exec(self.questions[self.index])
            self.index += 1

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
            self.onBaymaxResponse("शुभ प्रभात", "MANGAL")
        elif 12 <= hour < 17:
            self.speak.textToSpeech("namaskaar")
            self.onBaymaxResponse("नमस्कार", "MANGAL")
        else:
            self.speak.textToSpeech("namaskaar")
            self.onBaymaxResponse("नमस्कार", "MANGAL")

    def start(self):
        self.index = 0
        self.onBaymaxResponse("Please Select a Language: English / Hindi")
        self.onBaymaxResponse("कृपया एक भाषा चुनें: अंग्रेजी / हिंदी", "MANGAL")
        self.speak.textToSpeech("Please Select a Language: English or Hindi. Kripya eak Bhaashaaa Chunei: Angrezi yaa Hindi")

    def start1(self):
        self.language = self.data[0]
        self.language = self.language.lower()
        if self.language == "english":
            self.greetingEnglish()
            self.speak.textToSpeech("I'm Baymax, Your Personal Health Care companion. I need some of your personal "
                                    "details to serve you better. So, Let's get started. First of all What's your name?")
            self.onBaymaxResponse("I'm Baymax, Your Personal Health Care companion.")
            self.onBaymaxResponse("I need some of your personal details to serve you better.")
            self.onBaymaxResponse("So, Let's get started")
            self.onBaymaxResponse("What's your name?")
        else:
            self.greetingHindi()
            self.speak.textToSpeech("Mai Baymax, aapka swasthya dekhbhaal sahaayak. moojhe aapki koocch jaankaari ki"
                                    "zaroorat hai, Kripya apna naam batae")
            self.onBaymaxResponse("अपना नाम दर्ज करें: ", "MANGAL")

    def start2(self):
        if self.language == "english":
            self.speak.textToSpeech("What is your age")
            self.onBaymaxResponse("What is your age?")
        else:
            self.speak.textToSpeech("Hello " + self.data[1] + ", Aapki oomra kitni hai")
            self.onBaymaxResponse("कृपया अपनी उम्र दर्ज करें: ", "MANGAL")

    def start3(self):
        if self.language == "english":
            self.speak.textToSpeech("What are the symptoms that you are facing")
            self.onBaymaxResponse("What are the symptoms that you are facing...")
        else:
            self.speak.textToSpeech("Aapko kya pareshaniya ho rahi hai")
            self.onBaymaxResponse("कृपया अपने लक्षण दर्ज करें: ", "MANGAL")

    def processData(self):
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

    def arrangeData(self):
        self.name = self.data[1]
        self.age = self.data[2]

    def predictDisease(self):
        self.disease, self.confidence = self.tree.predict(self.processData())
        if self.confidence > 0.5:
            if self.language == "english":
                self.speak.textToSpeech(("There is " + str(self.confidence*100) + "percent chance that you might have "
                                         + str(self.disease)))
                self.onBaymaxResponse(("There is " + str(self.confidence*100) + "percent chance that "))
                self.onBaymaxResponse(("You might have " + str(self.disease)))
            else:
                self.speak.textToSpeech("Aapko" + str(self.disease) + "Hone ki " + str(self.confidence*100) +
                                        " pratishat ashanka hai.")
                self.onBaymaxResponse("आपको " + str(self.disease) + " होने की " + str(self.confidence*100) +
                                      " प्रतिशत आशंका है", "MANGAL")
        else:
            if self.language == "english":
                self.speak.textToSpeech("You just need some bed rest.")
                self.onBaymaxResponse("You just need some bed rest.")
            else:
                self.speak.textToSpeech("Aapko bas thode araam ki zarurat hai")
                self.onBaymaxResponse("आपको बस थोड़े आराम की ज़रूरत है")

    def predictMedication(self):
        if self.language == "english":
            self.speak.textToSpeech("Let me write you some medications.")
            self.onBaymaxResponse("Let me write you some medications.")
        else:
            self.speak.textToSpeech("Mai aapko kuch dawaiya likh deta hu.")
            self.onBaymaxResponse("मै आपको कुछ दवाइयां लिख देता हूँ", "MANGAL")
        self.medication = list()
        for item in self.symptoms:
            try:
                self.medication.append(DiseaseToMedicine.DrugName[item])
            except KeyError:
                pass
        try:
            self.medication.append(DiseaseToMedicine.DrugName[self.disease])
        except KeyError:
            pass

    def printPrescription(self):
        if self.language == "english":
            self.speak.textToSpeech("Your prescription is being printed.")
            self.onBaymaxResponse("Your prescription is being printed.")
        else:
            self.speak.textToSpeech("Aapka prescription print ho raha hai.")
            self.onBaymaxResponse("आपका प्रिस्क्रिप्शन प्रिंट हो रहा है.", "MANGAL")
        self.arrangeData()
        self.pdf = pdfgen.pdfGenerator(self.name, self.age, self.gender, self.disease, self.symptoms, self.medication)
        self.pdf.header()
        self.pdf.introduce()
        self.pdf.pdf_output()
    
    def startExportingToDatabase(self):
        self.arrangeData()
        self.DB = database.exportToDB(self.name, self.age, self.gender, self.disease, self.symptoms, self.medication)
        self.DB.export()

    def onHelpPress(self):
        self.speak.textToSpeech("kirpaya screen ke saamne sthir hokar baith jaae aur camera mein dekhe. Baymax ko challu"
                                " karne ke liye neeche daaein side mein jo start ka button hai wo dabaien. Baymax ke "
                                "sawwalon ka type karke ya bol ka javab dein.")
        self.speak.textToSpeech("Please sit in from of screen and see in the camera. Press start baymax button present "
                                "on lower righr side in screen. Answer the questions asked by baymax by typing or "
                                "speaking.")

    def onAnalyseButtonPress(self):
        self.plt.plotDB(self.name)
        self.plt.plotting()

# Actual window
class mainScreenApp(App):
    def build(self):
        self.title = "Baymax"
        self.icon = "./assets/icons/baymaxIcon.png"
        Window.fullscreen = 'auto'
        return mainScreenLayout()
