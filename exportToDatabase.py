# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:10:03 2021

@author: khuranagarvit019
"""

import mysql.connector
from mysql.connector import Error
import datetime

class exportToDB:
    def __init__ (self, name, age, sex, disease, symptoms=None, medications=None):
        self.datetime = datetime.datetime.now().replace(second=0, microsecond=0)
        self.datetime = str(datetime)
        self.name = name
        self.age = str(age)
        self.sex = sex
        self.disease = disease
        if symptoms is None:
            symptoms = []
        self.symptoms = symptoms
        x = ', '.join(map(str, self.symptoms))
        self.x = x
        self.disease = disease

        if medications is None:
            medications = []
        self.medications = medications
        y = ', '.join(map(str, self.medications))
        self.y = y
        self.host = 'sql12.freemysqlhosting.net'
        self.database = 'sql12394214'
        self.user = 'sql12394214'
        self.password = 'CJz7DFaZw1'
        
    def export(self):
        try:
            conn = mysql.connector.connect(self.host,self.database,self.user,self.password)
            
            if conn.is_connected():
                print("Connection with Database Successful")
                cursor = conn.cursor(buffered=True)
                
                insertQuery = "INSERT INTO patientDetails VALUES(%s, %s, %s, %s, %s, %s, %s)"
                values = (self.datetime, self.name, self.sex, self.age, self.x, self.disease, self.y)
                cursor.execute(insertQuery, values)

                conn.commit()
        except Error as e:
            print("Error while connecting to Database ", e)

        # closing database connection
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("Database connection closed.")
    
    