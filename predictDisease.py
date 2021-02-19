# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 04:16:21 2021

@author: khuranagarvit019
"""

import chatchat
import mainFuncOfTreeClassifier
from silence_tensorflow import silence_tensorflow
silence_tensorflow()

def startPredicting():
    gender,name,age,symptomListForPrediction = chatchat.start()
    mainFuncOfTreeClassifier.runFinalModel(symptomListForPrediction)
    predictedDisease = mainFuncOfTreeClassifier.runFinalModel()
    
    return (predictedDisease)

startPredicting()