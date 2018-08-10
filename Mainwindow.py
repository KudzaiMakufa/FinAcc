# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from datetime import datetime
import time
from Records import *
from Expenses import *



class Ui_MainWindow(object):
    def messagbx(self ,title , message, icon):

        icon = QtWidgets.QMessageBox.Warning if icon == '' else QtWidgets.QMessageBox.Information
        msgbx =QtWidgets.QMessageBox()
        msgbx.setIcon(icon)
        msgbx.setWindowTitle(title)
        msgbx.setText(message)
        msgbx.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgbx.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.calendarWidget = QtWidgets.QCalendarWidget(MainWindow)
        self.calendarWidget.setGeometry(QtCore.QRect(180, 40, 350, 187))
        self.calendarWidget.setObjectName("calendarWidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 240, 53, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 53, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 290, 53, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 410, 71, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 53, 19))
        self.label_5.setObjectName("label_5")
        self.chckEco = QtWidgets.QCheckBox(self.centralwidget)
        self.chckEco.setGeometry(QtCore.QRect(250, 450, 84, 25))
        self.chckEco.setObjectName("checkBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 450, 101, 19))
        self.label_6.setObjectName("label_6")
        self.chckCash = QtWidgets.QCheckBox(self.centralwidget)
        self.chckCash.setGeometry(QtCore.QRect(350, 450, 84, 25))
        self.chckCash.setObjectName("checkBox_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 510, 53, 19))
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 230, 350, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 280, 350, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 330, 350, 27))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 390, 350, 27))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 490, 350, 27))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.push_exp = QtWidgets.QPushButton(self.centralwidget)
        self.push_exp.setGeometry(QtCore.QRect(250, 610, 84, 27))
        self.push_exp.setObjectName("pushButton")

        self.btb_Rcrd = QtWidgets.QPushButton(self.centralwidget)
        self.btb_Rcrd.setGeometry(QtCore.QRect(450, 610, 80, 27))
        self.btb_Rcrd.setObjectName("pushButton")

        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(240, 550, 130, 32))
        self.btn_submit.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 610, 80, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 24))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuMenu.addAction(self.actionSettings)
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionHelp)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FinAcc By Kidkudzy"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Date"))
        self.label_3.setText(_translate("MainWindow", "District"))
        self.label_4.setText(_translate("MainWindow", "Reference"))
        self.label_5.setText(_translate("MainWindow", "Amount"))
        self.chckEco.setText(_translate("MainWindow", "Ecocash"))
        self.label_6.setText(_translate("MainWindow", "Payment mode"))
        self.chckCash.setText(_translate("MainWindow", "Cash"))
        self.label_7.setText(_translate("MainWindow", "Purpose"))
        self.btn_submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.btn_submit.clicked.connect(self.submit_data)

        self.btb_Rcrd.setText(_translate("MainWindow", "Records"))
        self.push_exp.setText(_translate("MainWindow", "Expenses"))
        self.push_exp.clicked.connect(self.expwindw)
        self.btb_Rcrd.clicked.connect(self.recordwin)

    def recordwin(self):

        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog1()
            self.ui.setupUi(self.window)
            MainWindow.show()

            self.window.show()
        except Exception as e:
            print('error')
        else:
            pass
        finally:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog1()
            self.ui.setupUi(self.window)
            MainWindow.hide()

            self.window.show()
            
        

        


    def expwindw(self):
        
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.window)
            MainWindow.hide()
            self.window.show()


    def check_decision(self, MainWindow):
        det = Ui_MainWindow.retranslateUi(self, MainWindow)
        
        if self.chckEco.isChecked():
            self.mode = 'Ecocash'
        if self.chckCash.isChecked():
            self.mode = 'Cash'
        elif self.chckEco.isChecked() == 0:
            self.mode = 'unspecified'
            


    def submit_data(self):
        det = Ui_MainWindow.check_decision(self, MainWindow)
                #date = (self.lineEdit.text())
        date =str(self.calendarWidget.selectedDate().toPyDate())   
        #date = self.calendarWidget.text()
        name = self.lineEdit_2.text()
        district = self.lineEdit_3.text()
        amount = self.lineEdit_4.text()
        reference = self.lineEdit_5.text()
        purpose = self.lineEdit_6.text()
        mode = self.mode

        conn = sqlite3.connect('Funds.db')

        c = conn.cursor()
        b = conn.cursor()

        # Create table
        #c.execute('''CREATE TABLE Funds
                    #(updated_at date, name text, district text, amount real, reference text, purpose text)''')

        # Insert a row of data


        if name == '' or district == '' or amount =='' or reference =='' or purpose =='':
            
            self.messagbx('Warning', 'Enter all Input Fields', '')
        elif self.mode != 'Ecocash' and self.mode !='Cash':
            self.messagbx('Warning', 'Tick Payment mode', '')
        else:

                
                try:
                        c.execute("INSERT INTO Funds VALUES ('"+date+"', '"+name+"','"+district+"','"+amount+"','"+reference+"', '"+purpose+"', '"+mode+"')")
                        b.execute("SELECT * FROM Funds WHERE name = '"+name+"'")
                        results = b.fetchone()
                        if results != 0:
                            print(type(results))
                            self.messagbx('Information', 'Records Inserted', 'info')
                            self.window = QtWidgets.QMainWindow()
                            self.ui = Ui_Dialog1()
                            self.ui.setupUi(self.window)
                            #MainWindow.hide()
                        
                            self.window.show()
                        else:
                            self.messagbx('Information', 'Data not Inserted!!! redirected to  Records','information')
                except Exception as e:
                    self.messagbx('warning', 'Unknown error report to developer ','')
                else:
                    pass
                finally:
                    
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_Dialog1()
                    self.ui.setupUi(self.window)
                    MainWindow.hide()
                
                    self.window.show()
                    
                
                    
        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with iaat.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

