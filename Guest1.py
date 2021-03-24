import sys
import os
import pywinauto
import autoit
import pyautogui
import time
import webbrowser
import win32gui
import subprocess
import shlex
import pynput
from typing import Union
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from time import sleep
from pywinauto.application import Application
from time import sleep
from pyautogui import press
from pyautogui import sleep
from pyautogui import getWindowsWithTitle
from pyautogui import getAllTitles
from pynput import keyboard
from pynput.keyboard import Listener
from pynput.keyboard import Key
from pynput import mouse
from pynput.mouse import Listener
from pynput.mouse import Button
from pynput.mouse import Controller

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle('Hello there')
        self.initUI()
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My label')
        self.label.move(50,50)

        self.button1=QtWidgets.QPushButton(self)
        self.button1.setText('pls dont click me')
        self.button1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.label.setText("OOF! You clicked me!")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

#execute function
window()