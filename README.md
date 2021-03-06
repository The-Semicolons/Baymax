# Baymax
Low budget solution for medical scarcity in rural/remote areas. The application is able to communicate with patients and diagnosing them properly.

[Check out Project Website!](https://baymax.ml/)

## Problem
The problem we are focussing on is Medical aid scarcity in rural, remote and even urban areas. Let us onsider the following cases:-
- ### Rural area
    A farmer from rural area got sick he needs diagnosis. He reaches out the nearest health centre constructed by govt. But he is unable to get diagnosed. Then the farmer heads to nearest city to get diagnosis. A farmer's whole day is wasted to get diagnosed along with travelling cost.
- ### Remote area
    A person from remote area got sick he needs diagnosis. He reaches out the nearest health centre constructed by govt. But he is unable to get diagnosed. Next he calls out city to get some transportation like ambulance/air ambulance, then get's transfered to a city hospital. Calling an ambulance/air ambulance cost enormous amount of money and time.
- ### Urban area
    A person in a city got sick he needs diagnosis. He reaches out the nearest health centre, But it takes enormous amount of time to get diagnosed by a doctor because of overcrowding in the doctor's clinic.

## Solution
The Health Assistant is capable of diagnosing diseases by taking voice/text/sign-language as an input of primary details of patients. The symptoms are processed using decision trees with Ada boost algorithm and thereby treatment is prescribed for the same. It detects their gender using Computer Vision and thus assigns the voice accordingly.
- ### Rural area
    In the above problem case, the farmer could have been diagnosed under few hours by installing our application in the health centre. He wouldn't have lost his time and money to travel to a city. The farmer just needed to tell baymax what are his symptoms, and baymex would have suggested him medicines and test as per the need.
- ### Remote area
    The person who got sick in the remote are could have been treetes at the nearest health centre by just telling baymax what his symptoms are. The cost and time for calling an ambulance/air ambulance could have been saved.
- ### Urban area
    It took enormous amount of time for the person to get diagnosed in the doctor's clinic. If doctor takes 10 minutes to diagnose a patient, it will take 100 minutes to diagnose 10. If Baymax is installed in doctor's clinic, it will take 10 minutes for doctor to see a patient and same 10 minutes for baymax. Then just another minute for doctor to verify baymax's diagnosis. So just 11 minutes to diagnose 2 patients hence total time to diagnose 10 patients is brought down to 55, saving 45 minutes of a doctor.

## Technology used
- ### Programming Language
    Python is selected to be the main programming language for our application because it has multiplatform support and is easy to work with in case of Machine learning applications.
- ### Tensorflow
    Tensorflow is used to construct the Decision tree with ada boost algorithm, also known as boosted tree classifier. The Decision tree is trained on a dataset that relates diseases to it's symptoms.
- ### Keras
    Keras is used to to create a DNN and was trained over 5000 images to detect the gender of a person sitting in front of Baymax.
- ### OpenCV
    OpenCV is used to capture the image, detect the face, process the image to make it suitable to be fed into DNN. Further DNN detects whether the person is male of female.
- ### Kivy
    Kivy is used to construct the GUI through kivy language. Kivy is preffered because of it's multi platform support and dynamic nature.
- ### NLTK
    NLTK is used for text processing and extract the usefull information from the user giving the user a human like interaction while talking to baymax.
- ### Google Voice
    Google voice API is used to recognise and translate what a user said to english which is then fed to language processor for further operations.
- ### Oracle's MySQL
    Oracle's MySQL is used to store and keep track of user's medical record including prescriptions, diagnosis and medical test reports.

## Uniqueness
- ### Multilingual
    Our application is able to interact with the patients in multiple languages including English, Hindi, Marathi, Bengali, Tamil, Telugu etc.
- ### Cross Platform
    The application is can be installed on multiple platforms like Windows, Mac, Linux and even android without any significant changes.
- ### Voice Recognition
    Baymax is able to understand what you are sying in any local language and can easily translate to any other language.
- ### Sign LAnguage Recognition
    For the people who are hearing and speech impaired can easily interact with baymax through sign language.
- ### Computer Vision
    Computer vision is used to make Baymax's interaction with human better by changing the voice of baymax to female voice for a female patient.
- ### Friendly GUI
    Gui on which the application is made is very simple and easy to use. Even if someone is stuck in between they click the "Help" button and Baymax will dictate how to use.
- ### Encrypted Database
    Oracle's MySQL is used to store all the critical information of the user. Though MySQL is an encrypted database all the patient's data is safe.