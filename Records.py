# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from Mainwindow import Ui_MainWindow

class Ui_Dialog1(object):

    def load_data(self):
        

        _translate = QtCore.QCoreApplication.translate
        connection = sqlite3.connect('Funds.db')
        query = ("SELECT * FROM Funds ORDER BY CURRENT_TIMESTAMP")
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)

        for row_number , row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        
        

        c = connection.cursor()
        tot = c.execute("SELECT SUM(amount) FROM Funds")
        getTot = tot.fetchone()

        print(getTot[0])

        exp = c.execute("SELECT SUM(amount) FROM Expenses")
        
        getExp = exp.fetchone()

        final = getTot[0] - getExp[0]
       
        print(final)
        



        self.lbl_Rrcd.setText(_translate("Dialog", str(getTot[0])))
        self.lbl_xptot.setText(_translate("Dialog", str(getExp[0])))
        self.label_fintot.setText(_translate("Dialog", str(final)))

        connection.close()




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 541)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 800, 461))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSizeAdjustPolicy(
        QtWidgets.QAbstractScrollArea.AdjustToContents)

        
        
        self.btn_load = QtWidgets.QPushButton(Dialog)
        self.btn_load.setGeometry(QtCore.QRect(10, 510, 151, 27))
        self.btn_load.setObjectName("btn_load")

        self.lbl_xptot = QtWidgets.QLabel(Dialog)
        self.lbl_xptot.setGeometry(QtCore.QRect(500, 510, 80, 27))
        self.lbl_xptot.setObjectName("btn_load")


        self.btn_back = QtWidgets.QPushButton(Dialog)
        self.btn_back.setGeometry(QtCore.QRect(170, 510, 100, 27))
        self.btn_back.setObjectName("btn_load")

        self.label_Bal = QtWidgets.QLabel(Dialog)
        self.label_Bal.setGeometry(QtCore.QRect(600, 510, 50, 27))
        self.label_Bal.setObjectName("label_2")

        self.label_fintot = QtWidgets.QLabel(Dialog)
        self.label_fintot.setGeometry(QtCore.QRect(650, 510, 100, 27))
        self.label_fintot.setObjectName("label_2")
    

        self.label_Tot = QtWidgets.QLabel(Dialog)
        self.label_Tot.setGeometry(QtCore.QRect(290, 510, 120, 27))
        self.label_Tot.setObjectName("label_2")


        self.explab = QtWidgets.QLabel(Dialog)
        self.explab.setGeometry(QtCore.QRect(420, 515, 60, 19))
        self.explab.setObjectName("label_2")

        
        self.lbl_Rrcd = QtWidgets.QLabel(Dialog)
        self.lbl_Rrcd.setGeometry(QtCore.QRect(360, 510, 60, 27))
        self.lbl_Rrcd.setObjectName("btn_load")
        

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #def expenz(self):
       # conn = sqlite3.connect('Funds.db')
        #c = conn.cursor()
        #c.execute("SELECT sum(amount) AS TOTAL FROM Expenses")
        #self.totalexp = c.fetchall()
        #self.totalexp = 'fuck you dude you thot i wld never call you from another function?'

    def clickMethod(self):
        from Mainwindow import Ui_MainWindow
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.window)
        self.window.close()
                
        #self.window.show()

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DEVELOPED BY PROMISE!!!"))
        self.btn_load.setText(_translate("Dialog", "Fetch Records"))
        self.label_Tot.setText(_translate("Dialog", "Received"))
        self.btn_back.setText(_translate("Dialog", "Back"))
        self.btn_back.clicked.connect(self.clickMethod)
        #self.btn_load.clicked.connect(self.xpenz)
        self.btn_load.clicked.connect(self.load_data)

        self.explab.setText(_translate("Dialog", "Expenses"))

        self.label_Bal.setText(_translate("Dialog", "Bal"))

        

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "District"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Reference"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Purpose"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "PayMode"))
        

    def closeit(self):
        try:
            #self.window = QtWidgets.QMainWindow()
            #self.ui = Ui_MainWindow()
            #self.ui.setupUi(self.window)
            #MainWindow.hide()
            pass

            #self.window.show()
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

