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
        self.conn = mysql.connector.connect(host = 'sql12.freemysqlhosting.net',
                                            database = 'sql12394214',
                                            user = 'sql12394214',
                                            password = 'CJz7DFaZw1')
        self.cursor = self.conn.cursor(buffered=True)
    def export(self):
        try:
            
            self.conn = mysql.connector.connect(host = 'sql12.freemysqlhosting.net',
                                                database = 'sql12394214',
                                                user = 'sql12394214',
                                                password = 'CJz7DFaZw1')
            if self.conn.is_connected():
                print("connection with Database Successful")
                self.cursor = self.conn.cursor(buffered=True)
                
                insertQuery = "INSERT INTO patientDetails VALUES(%s, %s, %s, %s, %s, %s, %s)"
                values = (self.datetime, self.name, self.sex, self.age, self.x, self.disease, self.y)
                self.cursor.execute(insertQuery, values)

                self.conn.commit()
        except Error as e:
            print("Error while connecting to Database ", e)

        # closing database connection
        finally:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print("Database connection closed.")

    