#Created by Vanshaj Goel 

import speech_recognition
from googletrans import Translator
import pyttsx3


class SpeechTextProcessing:
    def __init__(self, gender):
        self.r = speech_recognition.Recognizer()
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.translator = Translator()
        self.engine.setProperty('voice', self.voices[gender].id)

    def speechToText(self):
        with speech_recognition.Microphone() as source:
            audio = self.r.listen(source)

        try:
            RecoginisedText = self.r.recognize_google(audio)
            return RecoginisedText
        except speech_recognition.UnknownValueError:
            print("Could not understand audio, please speak clearly")
        except speech_recognition.RequestError as e:
            print("Could not request results! Contact developer")

    def textToSpeech(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def hindiToEnglish(self, text):
        translation = self.translator.translate(text, dest='en')
        return translation.text

    def englishToHindi(self, text):
        translation = self.translator.translate(text, src='en', dest='hi')
        return translation.text
