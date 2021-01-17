# Created By: Garvit Khurana on 28th December 2020

import pyttsx3
import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import mysql.connector
from mysql.connector import Error

# Setting Voice Engine for BayMax
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif 12 <= hour < 17:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")


# nltk.download()

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
    greeting()
    speak("Hello there!")
    speak("I'm Baymax, Your Personal Health Assistant")
    speak("I need some of your personal details to serve you better. So, Let's get started.")

    speak("What's your name?")
    sent1 = str(input("Please enter your name: "))
    words1 = word_tokenize(sent1)
    name = words1[len(words1) - 1]
    print("You have entered: ", name)

    speak("Hello " + name + ", Please tell your age")
    sent2 = input("Please enter your age: ")
    words2 = word_tokenize(sent2)
    age = words2[len(words2) - 1]
    print("You have entered: ", age)

    speak("Thanks for telling your age. Please tell your gender")
    sent3 = str(input("Please Enter Your Gender (M/F): "))
    words3 = word_tokenize(sent3)
    gender = words3[len(words3) - 1]
    print("You have entered: ", gender)

    speak("Please enter the symptoms you are facing")
    sent4 = str(input("Please enter your symptoms: "))
    # words4 = word_tokenize(sent4)
    # symptoms = words4[len(words4) - 1]
    symptoms = sent4
    print(symptoms)
    try:

        conn = mysql.connector.connect(host='sql12.freemysqlhosting.net',
                                       database='sql12384630',
                                       user='sql12384630',
                                       password='xRFJMdeWX9')

        if conn.is_connected():
            print("connected successfully")
            cursor = conn.cursor()
            cursor.execute("select * from health where symptoms like '%" + symptoms + "%'")
            record = cursor.fetchone()
            speak("Are you also suffering from " + record[2] + "?")
            sent5 = str(input("Are you also suffering from " + record[2] + "? (yes/no)"))
            words5 = word_tokenize(sent5)
            addedsymp = words5[0]
            for w in words5:
                if w not in stopWords:
                    filteredWords.append(w)
                    lemWords.append(ps.lemmatize(w))
            print(addedsymp)
            if addedsymp == no:
                speak("Then you have nothing to worry about, " + name + " Have a nice day!")

            elif addedsymp == y or addedsymp == yes:

                speak("You may be suffering from " + record[3] + " , but dont worry I've got your back")
                print("You may be suffering from " + record[3] + ".")

                speak("You can take the analgesics, " + record[4] + "for immediate relief and you can also go for, " + record[5])
                print("You can take the analgesics " + record[4] + " for immediate relief and you can also go for " + record[5])

                speak("Also, please don't forget to include good amounts of " + record[6] + " in your diet. ")
                print("Also, please don't forget to include good amounts of " + record[6] + " in your diet. ")

                speak("Hope that was helpful. It was nice serving you," + name)
                print("Hope that was helpful. It was nice serving you, " + name)

    except Error as e:
        print("Error while connecting to Database ",e)

    # closing database connection
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed.")


