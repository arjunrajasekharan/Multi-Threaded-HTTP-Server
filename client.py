# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
import socket
import os
import time

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 
host = "127.0.0.1"
port = 5001

linkTemplate = '<a href={0}>{1}</a>'

class HyperlinkLabel(QLabel):

    def __init__(self, parent=None):

        super().__init__()

        self.setStyleSheet('font-size: 25px')

        self.setOpenExternalLinks(True)

        self.setParent(parent)
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 791, 531))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        
        self.error1 = QtWidgets.QLabel(self.page1)
        self.error1.setGeometry(QtCore.QRect(30, 70, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.error1.setFont(font)
        self.error1.setObjectName("error1")
        
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setGeometry(QtCore.QRect(265, 120, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page1)
        self.label_2.setGeometry(QtCore.QRect(240, 240, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page1)
        self.lineEdit.setGeometry(QtCore.QRect(240, 290, 331, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton1 = QtWidgets.QPushButton(self.page1)
        self.pushButton1.setGeometry(QtCore.QRect(340, 360, 106, 30))
        self.pushButton1.setObjectName("pushButton1")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        
        self.error2 = QtWidgets.QLabel(self.page2)
        self.error2.setGeometry(QtCore.QRect(30, 70, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.error2.setFont(font)
        self.error2.setObjectName("error2")
        
        self.label_3 = QtWidgets.QLabel(self.page2)
        self.label_3.setGeometry(QtCore.QRect(210, 190, 500, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page2)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 260, 371, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton2 = QtWidgets.QPushButton(self.page2)
        self.pushButton2.setGeometry(QtCore.QRect(330, 380, 106, 30))
        self.pushButton2.setObjectName("pushButton2")
        self.stackedWidget.addWidget(self.page2)
        
        
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label_4 = QtWidgets.QLabel(self.page3)
        self.label_4.setGeometry(QtCore.QRect(220, 150, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.page3)
        self.comboBox.setGeometry(QtCore.QRect(320, 230, 96, 29))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton3 = QtWidgets.QPushButton(self.page3)
        self.pushButton3.setGeometry(QtCore.QRect(300, 360, 141, 31))
        self.pushButton3.setObjectName("pushButton3")
        self.stackedWidget.addWidget(self.page3)
        
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        
        self.error3 = QtWidgets.QLabel(self.page4)
        self.error3.setGeometry(QtCore.QRect(30, 70, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.error3.setFont(font)
        self.error3.setObjectName("error3")
        
        self.label_5 = QtWidgets.QLabel(self.page4)
        self.label_5.setGeometry(QtCore.QRect(170, 120, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page4)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 210, 381, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton4 = QtWidgets.QPushButton(self.page4)
        self.pushButton4.setGeometry(QtCore.QRect(320, 350, 106, 30))
        self.pushButton4.setObjectName("pushButton4")
        self.stackedWidget.addWidget(self.page4)
        
        
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.label_6 = QtWidgets.QLabel(self.page5)
        self.label_6.setGeometry(QtCore.QRect(240, 150, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        


        self.label_LINK = HyperlinkLabel(self.page5)
        self.label_LINK.setGeometry(QtCore.QRect(250, 260, 301, 50))
        self.label_LINK.setObjectName("label_LINK")
        
        
        
        self.stackedWidget.addWidget(self.page5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.stackedWidget.setCurrentWidget(self.page1)
        
        self.pushButton1.clicked.connect(self.pushButton_1)
        self.pushButton2.clicked.connect(self.pushButton_2)
        self.pushButton3.clicked.connect(self.pushButton_3)
        self.pushButton4.clicked.connect(self.pushButton_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WEB HOSTER"))
        self.label_2.setText(_translate("MainWindow", "ENTER YOUR DOMAIN NAME :"))
        self.pushButton1.setText(_translate("MainWindow", "CONFIRM"))
        self.label_3.setText(_translate("MainWindow", "ENTER YOUR HTML FILENAME :"))
        self.pushButton2.setText(_translate("MainWindow", "SEND"))
        self.label_4.setText(_translate("MainWindow", "IS THERE A CSS FILE  ?"))
        self.comboBox.setItemText(0, _translate("MainWindow", "NO"))
        self.comboBox.setItemText(1, _translate("MainWindow", "YES"))
        self.pushButton3.setText(_translate("MainWindow", "CONFIRM"))
        self.label_5.setText(_translate("MainWindow", "ENTER NAME OF CSS FILE :"))
        self.pushButton4.setText(_translate("MainWindow", "SEND"))
        self.label_6.setText(_translate("MainWindow", "HERE IS YOUR LINK :"))
        self.label_LINK.setText(_translate("MainWindow", "HEHE !!! http://link"))
        
        
        
    def pushButton_1(self):
        distname = self.lineEdit.text()
        notunique=True 
        while notunique:
            s.send(f"{distname}{SEPARATOR}".encode())
            received = s.recv(BUFFER_SIZE).decode()
            isunique = received.split(SEPARATOR)[0]
            if isunique == "YES" :
                notunique =False
                print("yes, name is unique")
                self.stackedWidget.setCurrentWidget(self.page2)
            else:
                print("not unique try again ")
                self.error1.setText("ERROR : Domain name - \""+ distname +"\" already in use ")
                self.lineEdit.setText("")
                break
                #self.stackedWidget.setCurrentWidget(self.page1)
        print(distname)
       
            
            
            
    def pushButton_2(self):
        filename = self.lineEdit_2.text()
        
        try:
            f=open(filename,"rb")
        except IOError:
            print("----------------------------\n\n")
            self.error2.setText("ERROR : File Not Found ")
        
        filesize = os.path.getsize(filename)
        s.send(f"{filesize}{SEPARATOR}".encode())
        
        discard=s.recv(BUFFER_SIZE)
        remsize =filesize

        
            
            
        isremaining =True
        while isremaining:
            if remsize>0 and remsize >=BUFFER_SIZE :
                bytes_read = f.read(BUFFER_SIZE)
                remsize-=BUFFER_SIZE
                s.send(bytes_read)
            elif remsize >0 and remsize <BUFFER_SIZE:
                bytes_read = f.read(remsize)
                s.send(bytes_read)
                remsize=0
                f.close()
                isremaining=False
                
        self.stackedWidget.setCurrentWidget(self.page3)
        
    def pushButton_3(self):
        iscss = self.comboBox.currentText()
        print(iscss)
        if iscss == "NO":
            s.send(f"NO{SEPARATOR}".encode())
            
            received = s.recv(BUFFER_SIZE).decode()
            link = received.split(SEPARATOR)[0]
            self.label_LINK.setText(linkTemplate.format('http://'+link, 'http://'+link))
            self.label_LINK.adjustSize()
            print("link : ",end="")
            print(link)
            #input("ENTER to exit")
            s.close()
            self.stackedWidget.setCurrentWidget(self.page5)
        else :
            s.send(f"YES{SEPARATOR}".encode())
            self.stackedWidget.setCurrentWidget(self.page4)
            
    def pushButton_4(self):
        filename = self.lineEdit_3.text()
        
        try:
            f=open(filename,"rb")
        except:
            self.error3.setText("ERROR : File Not Found")
            
        filesize = os.path.getsize(filename)
        s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}".encode())
        remsize =filesize
        discard=s.recv(BUFFER_SIZE)
        
            
        isremaining =True
        while isremaining:
            #print(f'{remsize} {filesize}')
            if remsize>0 and remsize >=BUFFER_SIZE :
                bytes_read = f.read(BUFFER_SIZE)
                remsize-=BUFFER_SIZE
                s.send(bytes_read)
                print("here1")
            elif remsize >0 and remsize <BUFFER_SIZE:
                bytes_read = f.read(remsize)
                s.send(bytes_read)
                remsize=0
                f.close()
                isremaining=False
                print("here2")
        f.close()
        
        received = s.recv(BUFFER_SIZE).decode()
        link = received.split(SEPARATOR)[0]
        self.label_LINK.setText(linkTemplate.format('http://'+link, 'http://'+link))
        self.label_LINK.adjustSize()
        print("link : ",end="")
        print(link)
        #input("ENTER to exit")
        s.close()
        
        self.stackedWidget.setCurrentWidget(self.page5)
        


if __name__ == "__main__":
    import sys
    
        
    s = socket.socket()
    print(f"[+] Trying to connect to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    
    
    app = QtWidgets.QApplication(sys.argv)
    
    style = """
        #MainWindow{
            background: black;
        }
        #page1{
            background: #262D37;
            
        }
        
         
        #label{
            color:yellow;
        }
        #label_2{
            color:grey;
        }
        #lineEdit{
            background:#696969;
        }
        #pushButton1{
            background:grey;
        }
        #page2{
            background: #262D37;
        }
        #label_3{
            color:grey;
        }
        #lineEdit_2{
            background:#696969;
        }
        #pushButton2{
            background:grey;
        }
        #page3{
            background: #262D37;
        }
        #lable_4{
            color:grey;
        }
        #comboBox{
            background:grey;
        }
        #pushButton3{
            background:grey;
        }
        #page4{
            background: #262D37;
        }
        #label_5{
            color:grey;
        }
        #lineEdit_3{
            background:#696969;
        }
        #pushButton4{
            background:grey;
        }
        #page5{
            background: #262D37;
        }
        #label_6{
            color:grey;
        }
        #label_LINK{
            color:red;
        }
        #error1{
            color:#9ACD32;
            
        }
        #error2{
            color:#9ACD32;
            
        }
        #error3{
            color:#9ACD32;
            
        }
    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

