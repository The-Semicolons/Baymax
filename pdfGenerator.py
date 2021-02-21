# File created by Tanya Malhotra
# Dated 20/02/2020

# Touched on 20/02/2020 by Tanya Malhotra

# Generating Patient Prescription in pdf format

import datetime
from fpdf import FPDF 
pdf = FPDF()   
pdf.add_page()

class pdfGenerator:
    def header(self):
        pdf.set_font("Arial", 'B', size = 28)    
        pdf.image('./assets/images/Baymax.jpg', x = 8, y = 1, w = 40, h = 30, type = '', link = '')
        pdf.cell(160, 10, txt = "Baymax", ln =1, align = 'C')

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
        y = '\n'.join(map(str, self.medications))
        self.y = y

    def introduce (self):
        pdf.set_font("Arial", size = 20)
        pdf.cell(90, 60, txt = "Date and time - " + self.datetime, ln = 5, align = 'L')
        pdf.cell(80, 60, txt = "Name - " + self.name, ln = 5, align = 'L') 
        pdf.cell(160, -58, txt = "Sex - " + self.sex, ln = 1, align = 'R')
        pdf.cell(60, 90, txt = "Age - " + self.age , ln = 1, align = 'L')
        pdf.cell(60, -48, txt = "Symptoms - " + self.x, ln = 1, align = 'L')
        pdf.set_font("Arial", 'B', size = 20)  
        pdf.cell(60, 80, txt = "Predicted disease - " + self.disease, ln = 1, align = 'L')
        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt="Prescribed medications - " + self.y, ln=1, align='L')

    def pdf_output(self):
        now = datetime.datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        output = str(self.name + dt_string) 
        pdf.output(output + ".pdf")
