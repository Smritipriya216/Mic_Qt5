from PyQt5.QtWidgets import QMainWindow,QLabel,QApplication,QPushButton,QLineEdit,QTextBrowser
from PyQt5 import uic
import sys

import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("mic.ui",self)
        
        self.text_browser = self.findChild(QTextBrowser,"textBrowser")
        self.line_edit = self.findChild(QLineEdit,"lineEdit")
        self.push_btn = self.findChild(QPushButton,"pushButton_2")
        self.mic_btn = self.findChild(QPushButton,"pushButton")

        self.line_edit.returnPressed.connect(self.display)
        self.push_btn.clicked.connect(self.clicker)
        self.mic_btn.clicked.connect(self.take_command)

        self.show()

    
    def display(self):
        self.txt=self.line_edit.text()
        self.text_browser.append(f'HI->{self.txt}')
        self.line_edit.setText("")
    
    def clicker(self):
        self.line_edit.setText("")
        self.text_browser.setText("<--->")

    
    def take_command(self):
        try:
            with sr.Microphone() as source:
                print("LISTENTING")
                self.text_browser.append(f'listenting')
                voice=listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command=command.replace('alexa','')
                    self.text_browser.append(f'alexa listening to your command'+'\n'+f'{command}')
                    print(command)
                    
        except:
            pass
        # return command

app=QApplication(sys.argv)
UIwindow=UI()
app.exec_()