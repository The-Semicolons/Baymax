#Created by Vanshaj Goel on 29th January 2021
#pip3 install SpeechRecognition
#pip3 install pyttsx3
#pip3 install googletrans==3.1.0a0
#File name- SpeechAndTextProcessing.py
#For Text To Speech--> You just need to make object of class "SpeechTextProcessing" and call the method "SpeechToText"
#Function will return the detected text, you need to make a variable to store and print the text
#For Text To Speech--> You need to create object and call the method "TextToSpeech" by passing text as argument
#For HindiToEnglish-->You need to create object and call the method "HindiToEnglish" by passing text(of any language)as argument
import speech_recognition
import pyttsx3
from googletrans import Translator
class SpeechTextProcessing:

    def __init__(self):
            self.r = speech_recognition.Recognizer()
            self.engine = pyttsx3.init('sapi5')
            self.voices = self.engine.getProperty('voices')
            self.translator = Translator()

    def SpeechToText(self):
        with speech_recognition.Microphone() as source:
            audio = self.r.listen(source)

        try:
            RecoginisedText = self.r.recognize_google(audio)
            return RecoginisedText
        except speech_recognition.UnknownValueError:
            print("Could not understand audio, please speak clearly")
        except speech_recognition.RequestError as e:
            print("Could not request results! Contact developer")

    def TextToSpeech(self, audio):
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.say(audio)
        self.engine.runAndWait()

    def HindiToEnglish(self,text):
        translation = self.translator.translate(text, dest='en')
        return translation.text