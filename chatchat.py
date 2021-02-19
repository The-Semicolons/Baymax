# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:27:24 2021

@author: khuranagarvit019
"""

import pyttsx3
import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import warnings
import SpeechAndTextProcessing as sp
import genderDetectionOpenCV as gd
import symptomList 


warnings.filterwarnings('ignore')

def greetingMaleEnglish():
    speak = sp.SpeechTextProcessing()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak.TextToSpeechMale("Good Morning!")
        print("Good Morning!")
    elif 12 <= hour < 17:
        speak.TextToSpeechMale("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak.TextToSpeechMale("Good Evening!")
        print("Good Evening!")
        
def greetingMaleHindi():
    speak = sp.SpeechTextProcessing()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak.TextToSpeechMale("Shubh Prabhaat")
        print("शुभ प्रभात")
    elif 12 <= hour < 17:
        speak.TextToSpeechMale("namaskaar")
        print("नमस्कार")
    else:
        speak.TextToSpeechMale("namaskaar")
        print("नमस्कार")        
        
def greetingFemaleEnglish():
    speak = sp.SpeechTextProcessing()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak.TextToSpeechFemale("Good Morning!")
        print("Good Morning!")
    elif 12 <= hour < 17:
        speak.TextToSpeechFemale("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak.TextToSpeechFemale("Good Evening!")
        print("Good Evening!")
        
def greetingFemaleHindi():
    speak = sp.SpeechTextProcessing()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak.TextToSpeechFemale("Shubh Prabhaat")
        print("शुभ प्रभात")
    elif 12 <= hour < 17:
        speak.TextToSpeechFemale("namaskaar")
        print("नमस्कार")
    else:
        speak.TextToSpeechFemale("namaskaar")
        print("नमस्कार")        

stopWords = set(stopwords.words('english'))
filteredWords = []
tags = []
lemWords = []
y = 'yes'
n = 'no'
no = 'nope'
yes = 'yeah'
ps = WordNetLemmatizer()
        
def start():
    speak = sp.SpeechTextProcessing()
    gender = gd.video()
    warnings.filterwarnings(action = "ignore")
    if(gender == "man"):
    
        print("Please Select a Language: English/Hindi \n कृपया एक भाषा चुनें:   अंग्रेजी / हिंदी")
        
        speak.TextToSpeechMale("Please Select a Language: English/Hindi")
        speak.TextToSpeechMale("Kripya eak Bhaashaaa Chunei: Angrezi yaa Hindi")
        language = input("")
        lang = language.lower()
        if (lang == "english"):
            greetingMaleEnglish()
            speak.TextToSpeechMale("Hello there!")
            speak.TextToSpeechMale("I'm Baymax, Your Personal Health Assistant")
            speak.TextToSpeechMale("I need some of your personal details to serve you better. So, Let's get started.")

            speak.TextToSpeechMale("What's your name?")
            sent1 = str(input("Please enter your name: "))
            words1 = word_tokenize(sent1)
            name = words1[len(words1) - 1]
            print("You have entered: ", name)

            speak.TextToSpeechMale("Hello " + name + ", Please tell your age")
            sent2 = input("Please enter your age: ")
            words2 = word_tokenize(sent2)
            age = words2[len(words2) - 1]
            print("You have entered: ", age)
         
            speak.TextToSpeechMale("Please enter the symptoms you are facing")
            sent4 = str(input("Please enter your symptoms: "))
    # words4 = word_tokenize(sent4)
    # symptoms = words4[len(words4) - 1]
            symptoms = sent4
            print(symptoms)
            
        if (lang == "hindi"):
            greetingMaleHindi()
            
            speak.TextToSpeechMale("Mai Baymax, aapka swasthya dekhbhaal sahaayak")
            speak.TextToSpeechMale("moojhe aapki koocch jaankaari ki zaroorat hai")

            speak.TextToSpeechMale("aapkaa Naam Kya Hai?")
            sent1 = str(input("अपना नाम दर्ज करें: "))
            words1 = word_tokenize(sent1)
            name = words1[len(words1) - 1]
            print("You have entered: ", name)

            speak.TextToSpeechMale("Hello " + name + ", Kripyaa Apni oomra daalien")
            sent2 = input("कृपया अपनी उम्र दर्ज करें: ")
            conv = speak.HindiToEnglish(sent2)
            words2 = word_tokenize(conv)
            age = words2[len(words2) - 1]
            print("You have entered: ", age)
         
            speak.TextToSpeechMale("Kripyaa apne lakshan daalien")
            sent4 = str(input("कृपया अपने लक्षण दर्ज करें: "))
            conv = speak.HindiToEnglish(sent4)
    # words4 = word_tokenize(sent4)
    # symptoms = words4[len(words4) - 1]
            symptoms = conv
            print(symptoms)
    
    if(gender == "woman"):
    
        print("Please Select a Language: English/Hindi \n कृपया एक भाषा चुनें:   अंग्रेजी / हिंदी")
        
        speak.TextToSpeechFemale("Please Select a Language: English/Hindi")
        speak.TextToSpeechFemale("Kripya eak Bhaashaaa Chunei: Angrezi yaa Hindi")
        language = input("")
        lang = language.lower()
        if (lang == "english"):
            greetingFemaleEnglish()
            speak.TextToSpeechFemale("Hello there!")
            speak.TextToSpeechFemale("I'm Baymax, Your Personal Health Assistant")
            speak.TextToSpeechFemale("I need some of your personal details to serve you better. So, Let's get started.")

            speak.TextToSpeechFemale("What's your name?")
            sent1 = str(input("Please enter your name: "))
            words1 = word_tokenize(sent1)
            name = words1[len(words1) - 1]
            print("You have entered: ", name)

            speak.TextToSpeechFemale("Hello " + name + ", Please tell your age")
            sent2 = input("Please enter your age: ")
            words2 = word_tokenize(sent2)
            age = words2[len(words2) - 1]
            print("You have entered: ", age)
         
            speak.TextToSpeechFemale("Please enter the symptoms you are facing")
            sent4 = str(input("Please enter your symptoms: "))
    # words4 = word_tokenize(sent4)
    # symptoms = words4[len(words4) - 1]
            symptoms = sent4
            print(symptoms)
            
        if (lang == "hindi"):
            greetingFemaleHindi()
            
            speak.TextToSpeechFemale("Mai Baymax, aapka swasthya dekhbhaal sahaayak")
            speak.TextToSpeechFemale("moojhe aapki koocch jaankaari ki zaroorat hai")

            speak.TextToSpeechFemale("aapkaa Naam Kya Hai?")
            sent1 = str(input("अपना नाम दर्ज करें: "))
            words1 = word_tokenize(sent1)
            name = words1[len(words1) - 1]
            print("You have entered: ", name)

            speak.TextToSpeechFemale("Hello " + name + ", Kripyaa Apni oomra daalien")
            sent2 = input("कृपया अपनी उम्र दर्ज करें: ")
            conv = speak.HindiToEnglish(sent2)
            words2 = word_tokenize(conv)
            age = words2[len(words2) - 1]
            print("You have entered: ", age)
         
            speak.TextToSpeechFemale("Kripyaa apne lakshan daalien")
            sent4 = str(input("कृपया अपने लक्षण दर्ज करें: "))
            conv = speak.HindiToEnglish(sent4)
    # words4 = word_tokenize(sent4)
    # symptoms = words4[len(words4) - 1]
            symptoms = conv
            print(symptoms)
    
    patientSymptoms = symptoms.split()
    patientSymptomsFinal = [i.lower() for i in patientSymptoms]
    allSymptoms = symptomList.symptomList()
    
    symptomListForPrediction = []
    for i in range(131):
        symptomListForPrediction.append(0)
    for i in range(len(patientSymptomsFinal)):
        for j in range(131):
            if (patientSymptomsFinal[i] == allSymptoms[j]):
                symptomListForPrediction[j] = 1
    
    return(gender, name, age, symptomListForPrediction)