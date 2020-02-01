from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt
from PyQt4 import QtGui
from PyQt4.QtTest import QTest
from PyQt4 import QtTest
from random import choice
from string import ascii_lowercase, ascii_uppercase
from helper_sql import sqlQuery, sqlExecute
from bmconfigparser import BMConfigParser
import random 


class Testing:
    def __init__(self):
        self.inbox_length = sqlQuery("Select msgid from inbox")

    def label_generation(self, myapp):
        self.sleeper()
        myapp.ui.pushButtonNewAddress.setStyleSheet('QPushButton {background-color: red; color: white;}')
        QtTest.QTest.qWait(70)
        myapp.ui.pushButtonNewAddress.setStyleSheet("")
        QTest.mouseClick(myapp.ui.pushButtonNewAddress, Qt.LeftButton)
        self.sleeper()

    def address_autofill(self):
        self.sleeper()
        return choice(ascii_uppercase) + (''.join(choice(ascii_lowercase) for i in range(14)))

    def senf_functionality(self, myapp):
        myapp.ui.tabWidget.setCurrentWidget(myapp.ui.send)
        self.sleeper()
        if BMConfigParser().addresses():
            addresses = BMConfigParser().addresses()
        len_addresses = len(addresses)
        a = ""
        rand_var = random.randrange(1, len_addresses + 1)
        rand_address = random.choice(addresses)
        myapp.ui.comboBoxSendFrom.setCurrentIndex(rand_var)
        self.sleeper()
        for x in range(len(rand_address)):
            a = a + rand_address[x]
            myapp.ui.lineEditTo.setText(a)
            QtTest.QTest.qWait(1)    
        self.sleeper()
        a = ""
        for x in range(40):
            a = a + choice(ascii_lowercase)
            myapp.ui.lineEditSubject.setText(a)
            QtTest.QTest.qWait(1)
        self.sleeper()
        a = ""
        for x in range(200):
            a = a + choice(ascii_lowercase)
            myapp.ui.textEditMessage.setText(a)
            QtTest.QTest.qWait(1)
        self.sleeper()
        QTest.mouseClick(myapp.ui.pushButtonSend, Qt.LeftButton)
        self.sleeper()
        myapp.ui.tabWidget.setCurrentWidget(myapp.ui.inbox)
        QtTest.QTest.qWait(4000)
        new_msg_index = len(self.inbox_length) + 1
        inbox_length = sqlQuery("Select msgid from inbox")
        if len(inbox_length) == new_msg_index:
            msg = QtGui.QMessageBox()
            msg.setText("SUCESS!!~~")
            msg.setInformativeText("MESSAGE RECEIVED!")
            msg.setWindowTitle("MessageBox demo")
            msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            msg.show()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GOT MESSAGE!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("TEST FAILED!!")
        print("DONE!!")
    
    def subscriptions(self, myapp):
        self.sleeper()
        myapp.ui.tabWidget.setCurrentWidget(myapp.ui.subscriptions)
        QTest.mouseClick(myapp.ui.pushButtonAddSubscription, Qt.LeftButton)

    def sleeper(self):
        QtTest.QTest.qWait(1200)
