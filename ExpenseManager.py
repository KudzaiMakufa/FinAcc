# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableexpos.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):

	def load_data(self): 
		connection = sqlite3.connect('Funds.db')

		date = str(self.calendarWidget.selectedDate().toPyDate())

		_translate = QtCore.QCoreApplication.translate
		
	    
		query  = ("SELECT * FROM Expenses WHERE updated_at = '"+date+"'")
	    
		print(date)
		result = connection.execute(query)
	    
		self.tableWidget.setRowCount(0)

		for row_number , row_data in enumerate(result):
			self.tableWidget.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))


		c = connection.cursor()
		c.execute("SELECT sum(amount) FROM Expenses")
		self.getTot = c.fetchone()       
	    

		connection.close()

	def setupUi(self, Dialog):
	    Dialog.setObjectName("Dialog")
	    Dialog.resize(654, 600)
	    self.centralwidget = QtWidgets.QWidget(Dialog)
	    self.centralwidget.setObjectName("centralwidget")
	    self.pushButton = QtWidgets.QPushButton(self.centralwidget)
	    self.pushButton.setGeometry(QtCore.QRect(10, 70, 131, 27))
	    self.pushButton.setObjectName("pushButton")
	    self.dateEdit_3 = QtWidgets.QDateEdit(self.centralwidget)
	    self.dateEdit_3.setGeometry(QtCore.QRect(490, 10, 110, 28))
	    self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 8, 1), QtCore.QTime(0, 0, 0)))
	    self.dateEdit_3.setObjectName("dateEdit_3")
	    self.dateEdit_4 = QtWidgets.QDateEdit(self.centralwidget)
	    self.dateEdit_4.setGeometry(QtCore.QRect(260, 10, 110, 28))
	    self.dateEdit_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 8, 1), QtCore.QTime(0, 0, 0)))
	    self.dateEdit_4.setObjectName("dateEdit_4")
	    self.label_3 = QtWidgets.QLabel(self.centralwidget)
	    self.label_3.setGeometry(QtCore.QRect(150, 10, 53, 19))
	    self.label_3.setObjectName("label_3")
	    self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
	    self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 80, 27))
	    self.pushButton_2.setObjectName("pushButton_2")
	    self.label_4 = QtWidgets.QLabel(self.centralwidget)
	    self.label_4.setGeometry(QtCore.QRect(410, 10, 53, 19))
	    self.label_4.setObjectName("label_4")
	    self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
	    self.tableWidget.setGeometry(QtCore.QRect(280, 80, 331, 421))
	    self.tableWidget.setObjectName("tableWidget")
	    self.tableWidget.setColumnCount(3)
	    self.tableWidget.setRowCount(0)
	    item = QtWidgets.QTableWidgetItem()
	    self.tableWidget.setHorizontalHeaderItem(0, item)
	    item = QtWidgets.QTableWidgetItem()
	    self.tableWidget.setHorizontalHeaderItem(1, item)
	    item = QtWidgets.QTableWidgetItem()
	    self.tableWidget.setHorizontalHeaderItem(2, item)
	    self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
	    self.pushButton_3.setGeometry(QtCore.QRect(20, 470, 80, 35))
	    self.pushButton_3.setObjectName("pushButton_3")
	    self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
	    self.pushButton_4.setGeometry(QtCore.QRect(160, 470, 80, 35))
	    self.pushButton_4.setObjectName("pushButton_4")
	    self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
	    self.pushButton_5.setGeometry(QtCore.QRect(20, 380, 80, 35))
	    self.pushButton_5.setObjectName("pushButton_5")
	    self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
	    self.pushButton_6.setGeometry(QtCore.QRect(160, 380, 80, 35))
	    self.pushButton_6.setObjectName("pushButton_6")
	    self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
	    self.calendarWidget.setGeometry(QtCore.QRect(10, 120, 264, 170))
	    self.calendarWidget.setObjectName("calendarWidget")
	    self.label = QtWidgets.QLabel(self.centralwidget)
	    self.label.setGeometry(QtCore.QRect(20, 100, 53, 16))
	    self.label.setObjectName("label")
	    

	    self.retranslateUi(Dialog)
	    QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
	    _translate = QtCore.QCoreApplication.translate
	    Dialog.setWindowTitle(_translate("Dialog", "EXPENSE MANAGEMENT"))
	    self.pushButton.setText(_translate("Dialog", "Expense by Date"))
	    self.label_3.setText(_translate("Dialog", "From"))
	    self.pushButton_2.setText(_translate("Dialog", "Delete"))
	    self.label_4.setText(_translate("Dialog", "To"))
	    item = self.tableWidget.horizontalHeaderItem(0)
	    item.setText(_translate("Dialog", "amount"))
	    item = self.tableWidget.horizontalHeaderItem(1)
	    item.setText(_translate("Dialog", "Updated At "))
	    item = self.tableWidget.horizontalHeaderItem(2)
	    item.setText(_translate("Dialog", "Narration"))
	    self.pushButton_3.setText(_translate("Dialog", "Close"))
	    self.pushButton_4.setText(_translate("Dialog", "Back"))
	    self.pushButton_5.setText(_translate("Dialog", "Menu"))
	    self.pushButton_6.setText(_translate("Dialog", "All Expenses"))
	    self.label.setText(_translate("Dialog", "From :"))
	    #self.pushButton.clicked.connect(self.load_data(str(self.calendarWidget.selectedDate().toPyDate())))
	    self.pushButton.clicked.connect(self.load_data)
	    self.pushButton_6.clicked.connect(self.date2)

	def date2(self):
		date = str(self.calendarWidget.selectedDate().toPyDate())
	    

		_translate = QtCore.QCoreApplication.translate
		connection = sqlite3.connect('Funds.db')
	    
		query  = ("SELECT * FROM Expenses")
	    
		print(date)
		result = connection.execute(query)
	    
		self.tableWidget.setRowCount(0)

		for row_number , row_data in enumerate(result):
			self.tableWidget.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
	    
	    
		c = connection.cursor()
		c.execute("SELECT sum(amount) FROM Expenses")
		self.getTot = c.fetchone()       
	    

		connection.close()

	def fetchallxp(self,datei):
	    #datei = "30"
		print(datei)

	    

	def fetchqry(self ,deti):
	    #if deti =
	    pass


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())