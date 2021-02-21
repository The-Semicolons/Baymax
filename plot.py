import matplotlib.pyplot as plt

class graph:
    def __init__ (self, list1 = None, list2 = None):
        if list1 is None:
            list1 = []
        self.list1 = list1
        if list2 is None:
            list2 = []
        self.list2 = list2

    def plotting (self):
        plt.ylim(0, 5)
        plt.xlim(0,5)
        plt.plot(self.list1, label = 'calculated value')
        plt.legend()
        plt.plot(self.list2, label = 'ideal value')
        plt.legend()
        plt.title('Leucocyte Count')
        plt.show()
        


calc = [2.5, 4, 3.1, 2.9, 3.3]
ideal = [3, 3, 3, 3, 3]
obj = graph(calc, ideal)
obj.plotting()
# =============================================================================
# 
# 
# 
#  def plotDB(self):
#         try:
#             self.conn = mysql.connector.connect(self.host,self.database,self.user,self.password)
#             
#             if self.conn.is_connected():
#                 print("Connection with Database Successful")
#                 cursor = self.conn.cursor(buffered=True)
#                 name = input("Enter Patient Name: ")
#                 cursor.execute("select * from patientHistory where patientName like '%"+name+"%'")
#                 record = cursor.fetchone()
#                 print(record[0])
#                 self.conn.commit()
#         except Error as e:
#             print("Error while connecting to Database ", e)
# 
#         # closing database connection
#         finally:
#             if self.conn.is_connected():
#                 cursor.close()
#                 self.conn.close()
#                 print("Database connection closed.")
#         
# host = 'sql12.freemysqlhosting.net'
# database = 'sql12394214'
# user = 'sql12394214'
# password = 'CJz7DFaZw1'
# conn = mysql.connector.connect(host,database,user,password)
# =============================================================================
