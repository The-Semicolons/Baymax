#Created by Vanshaj Goel on 29th January 2021
#pip3 install SpeechRecognition
#File name- SpeechAndTextProcessing.py
#You just need to make object of class "SpeechTextProcessing" and call the function "TextToSpeech"
#Function will return the detected text, you need to make a variable to store and print the text
import speech_recognition as sr

class SpeechTextProcessing:
    def SpeechToText(self):
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tell your symptoms!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            RecoginisedText = r.recognize_google(audio)
            return RecoginisedText
        except sr.UnknownValueError:
            RecoginisedText="Could not understand audio, please speak clearly"
            return RecoginisedText
        except sr.RequestError as e:
            RecoginisedText="Could not request results! Contact developer of this software {0}".format(e)
            return RecoginisedText