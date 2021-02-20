# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 04:16:21 2021

@author: khuranagarvit019
"""

import chatchat
import SpeechAndTextProcessing
from silence_tensorflow import silence_tensorflow
silence_tensorflow()

speak = SpeechAndTextProcessing.SpeechTextProcessing()
def startPredicting():
    gender,name,age,symptomListForPrediction = chatchat.start()
    print("Processing... Wait for 1-2 Minutes")
    print("कृप्या... 1-2  मिनट तक प्रतीक्षा करें")
    speak.TextToSpeechFemale("Processing... Wait for 1-2 Minutes")
    speak.TextToSpeechFemale("Kripya eak - dow minute prateekshaa krien")
    
    predictedDisease = mainFuncOfTreeClassifier.runFinalModel(symptomListForPrediction)
    
    return (predictedDisease)