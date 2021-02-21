import matplotlib.pyplot as plt
import mysql.connector 
from mysql.connector import Error
class graph:
    def __init__ (self, list1 = None, list2 = None):
        if list1 is None:
            list1 = []
        self.list1 = list1
        if list2 is None:
            list2 = []
        self.list2 = list2
        self.host = 'sql12.freemysqlhosting.net'
        self.database = 'sql12394214'
        self.user = 'sql12394214'
        self.password = 'CJz7DFaZw1'
        self.conn = mysql.connector.connect(host = 'sql12.freemysqlhosting.net',
                                            database = 'sql12394214',
                                            user = 'sql12394214',
                                            password = 'CJz7DFaZw1')
        self.cursor = self.conn.cursor(buffered=True)

    def plotDB(self, name):
        try:
            
            self.conn = mysql.connector.connect(host = 'sql12.freemysqlhosting.net',
                                                database = 'sql12394214',
                                                user = 'sql12394214',
                                                password = 'CJz7DFaZw1')
            if self.conn.is_connected():
                print("connection with Database Successful")
                self.cursor = self.conn.cursor(buffered=True)
                self.cursor.execute("select * from patientHistory where patientName like '%" + name + "%'")
                record = self.cursor.fetchone()
                for i in range(0,12):
                    self.list1.append(record[i])
            
                self.conn.commit()
        except Error as e:
            print("Error while connecting to Database ", e)

        # closing database connection
        finally:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print("Database connection closed.")
        print(self.list1)
        return self.list1




    def plotting (self):
        plt.ylim(0,12)
        plt.xlim(0,12)
        plt.plot(self.list1, label = 'Patient RBC')
        plt.legend()
        self.list2 = [5,5,5,5,5,5,5,5,5,5,5,5]
        plt.plot(self.list2, label = 'Standard Value of RBC')
        plt.legend()
        plt.title('Red Blood Cell Count')
        plt.show()
        
        return plt.show()
