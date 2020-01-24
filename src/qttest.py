# import pyqt_code as pc
import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
from PyQt4 import QtGui
from pytestqt import qtbot
from PyQt4.QtTest import QTest
import pytestqt
import pytest
from bitmessageqt import settingsmixin


class PyTest(QtGui.QWidget):

    def __init__(self, app):
        super(PyTest, self).__init__()
        self.initUI(app)

    def initUI(self, app):
        # from bitmessageqt import bitmessageui
        # MainWindow = settingsmixin.SMainWindow()
        # ui = bitmessageui.Ui_MainWindow()
        # x = ui.setupUi(MainWindow)
        import pdb; pdb.set_trace()
        import bitmessageqt

        import pdb; pdb.set_trace()
        # qtbot._add_widget(self, QtGui.QLabel("S"))
        # qtbot._add_widget(self, QtGui.QPushButton("JJJJ"))
        self.hidewindow()
        x.titleEdit.setText("TEST1")
        x.authorEdit.setText("AUTHOR1")
        x.reviewEdit.setText("REVIEW1")
        QTest.mouseClick(x.btn1, Qt.LeftButton)
        self.hidewindow()

        x.titleEdit.setText("WWWWWWWWWWWWWWWWW")
        x.authorEdit.setText("WWWWWWWWWWWWWWWWW")
        x.reviewEdit.setText("WWWWWWWWWWWWWWWWW")
        # x.btn1.clicked.connect(self.hidewindow)
        QTest.mouseClick(x.btn1, Qt.LeftButton)
        self.hidewindow()

        x.titleEdit.setText("QQQQQQQQQQQQQQQQQQQ")
        x.authorEdit.setText("QQQQQQQQQQQQQQQQQQQ")
        x.reviewEdit.setText("QQQQQQQQQQQQQQQQQQQ")
        # x.btn1.clicked.connect(self.hidewindow)
        QTest.mouseClick(x.btn1, Qt.LeftButton)
        self.hidewindow()

        x.titleEdit.setText("YYYYYYYYYYYYYYYYY")
        x.authorEdit.setText("YYYYYYYYYYYYYYYYY")
        x.reviewEdit.setText("YYYYYYYYYYYYYYYYY")
        x.btn1.clicked.connect(self.hidewindow)
        QTest.mouseClick(x.btn1, Qt.LeftButton)
        sys.exit(app.exec_())
        # print(x.title.text())
    
    def hidewindow(self):
        x = pc.Example()
        import time
        time.sleep(1)
        x.titleEdit.hide()
        x.authorEdit.hide()
        x.reviewEdit.hide()
        print("HIDE!!")
        # return


def main():
    app = QtGui.QApplication(sys.argv)
    ex = PyTest(app)


if __name__ == '__main__':
    main()

# import pyqt_code as pc
# import sys
# import unittest
# from PyQt4.QtGui import QApplication
# from PyQt4.QtTest import QTest
# from PyQt4.QtCore import Qt
# from PyQt4 import QtGui
# from pytestqt import qtbot
# import pytestqt
# import pytest


# class PyTest(QtGui.QWidget):

#     def __init__(self, app):
#         super(PyTest, self).__init__()
#         self.initUI(app)

#     def initUI(self, app):
#         x = pc.Example()
#         from PyQt4.QtTest import QTest
#         qtbot._add_widget(self, QtGui.QLabel("S"))
#         qtbot._add_widget(self, QtGui.QPushButton("JJJJ"))
#         x.titleEdit.setText("TITLE11")
#         x.authorEdit.setText("AUTHORRR!!!")
#         x.reviewEdit.setText("REVIEW!!!!@@@@@@@@@@")
#         x.titleEdit.setText("TITLE11@@@@")
#         x.authorEdit.setText("AUTHORRR!!@@@@!")
#         x.reviewEdit.setText("REVIEW!!!!@@@@@@@@@@")
#         QTest.mouseClick(x.btn1, Qt.LeftButton)
#         sys.exit(app.exec_())
#         # print(x.title.text())


# def main():
#     app = QtGui.QApplication(sys.argv)
#     ex = PyTest(app)


# if __name__ == '__main__':
#     main()