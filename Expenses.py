# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expenses.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import *
import sqlite3


class Ui_Dialog(object):
    def messagbx(self ,title , message, icon):

        icon = QtWidgets.QMessageBox.Warning if icon == '' else QtWidgets.QMessageBox.Information
        msgbx =QtWidgets.QMessageBox()
        msgbx.setIcon(icon)
        msgbx.setWindowTitle(title)
        msgbx.setText(message)
        msgbx.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgbx.exec_()    
    def load_data(self):
        _translate = QtCore.QCoreApplication.translate
        connection = sqlite3.connect('Funds.db')
        query = ("SELECT * FROM Expenses ORDER BY CURRENT_TIMESTAMP")
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)

        for row_number , row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        
        
        c = connection.cursor()
        c.execute("SELECT sum(amount) FROM Expenses")
        getTot = c.fetchone()
        self.pushButton_4.setText(_translate("Dialog", str(getTot[0])))
        

        connection.close()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 535)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 201, 21))
        self.label.setObjectName("label")
        self.label_amnt = QtWidgets.QLabel(Dialog)
        self.label_amnt.setGeometry(QtCore.QRect(50, 270, 61, 19))
        self.label_amnt.setObjectName("label_amnt")
        self.label_narr = QtWidgets.QLabel(Dialog)
        self.label_narr.setGeometry(QtCore.QRect(50, 320, 61, 19))
        self.label_narr.setObjectName("label_narr")
        self.lineEdit_amnt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_amnt.setGeometry(QtCore.QRect(160, 270, 141, 27))
        self.lineEdit_amnt.setObjectName("lineEdit_amnt")
        self.btn_update = QtWidgets.QPushButton(Dialog)
        self.btn_update.setGeometry(QtCore.QRect(50, 480, 80, 27))
        self.btn_update.setObjectName("btn_update")
        self.btn_trial = QtWidgets.QPushButton(Dialog)
        self.btn_trial.setGeometry(QtCore.QRect(170, 480, 80, 27))
        self.btn_trial.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 480, 80, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 480, 80, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_amnt_2 = QtWidgets.QLabel(Dialog)
        self.label_amnt_2.setGeometry(QtCore.QRect(50, 70, 61, 19))
        self.label_amnt_2.setObjectName("label_amnt_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(160, 40, 381, 187))
        self.calendarWidget.setObjectName("calendarWidget")
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 320, 361, 70))
        self.textEdit.setObjectName("textEdit")
        self.promise = QtWidgets.QMessageBox(Dialog)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "UPDATE EXPENSES"))
        self.label_amnt.setText(_translate("Dialog", "Amount"))
        self.label_narr.setText(_translate("Dialog", "Narrration"))
        self.lineEdit_amnt.setPlaceholderText(_translate("Dialog", "$"))
        self.btn_update.setText(_translate("Dialog", "Post Expense"))
        self.btn_trial.setText(_translate("Dialog", "Manage"))
        self.pushButton_3.setText(_translate("Dialog", "close"))
        self.pushButton_4.setText(_translate("Dialog", "Help"))
        self.label_amnt_2.setText(_translate("Dialog", "Date"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Expenses:"))
        self.btn_update.clicked.connect(self.exp_updt)
    
        self.btn_trial.clicked.connect(self.clickMethod)
       

    def clickMethod(self):
        from ExpenseManager import Ui_Dialog
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        #Dialog.close()
                
        self.window.show()
    
    def exp_updt(self):
        conn = sqlite3.connect('Funds.db')
        exp_amnt = self.lineEdit_amnt.text()
        varnarration = self.textEdit.text()
        c = conn.cursor()
        #c.execute('''CREATE TABLE Expenses
                    #(updated_at date, amount real, narration text)''')
        if exp_amnt =='' or varnarration == '' :
            print('its empty')
            self.messagbx('Warning' ,'Empty Name and Narration', '')
            
        elif exp_amnt == str(c.execute("SELECT * FROM Expenses WHERE amount = '"+exp_amnt+"' ").fetchone()) :
            self.messagbx('Warning' ,'Amount Exist', '')

        else:
            c.execute("INSERT INTO Expenses VALUES (CURRENT_TIMESTAMP, '"+exp_amnt+"','"+varnarration+"')")
            conn.commit()
            conn.close()
            print('inserted')
            self.messagbx('Information' ,'Inserted into database', 'insert')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

