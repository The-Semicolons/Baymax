#Created by Vanshaj Goel on 29th January 2021
#pip3 install SpeechRecognition
#File name- Speech_To_Text.py
#You just need to make object of class "SpeechToText" and call the function "ProcessSpeech"
#Function will automatically print the detected text, you need not to make any print command
import speech_recognition as sr

class SpeechToText:
    def ProcessSpeech(self):
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
            text = r.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            text="Could not understand audio, please speak clearly"
            print(text)
        except sr.RequestError as e:
            text="Could not request results! Contact developer of this software {0}".format(e)
            print(text)