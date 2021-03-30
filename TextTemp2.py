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
import PIL
from PIL import Image
from PIL.ImageQt import ImageQt
import tkinter
from tkinter import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from time import sleep
import datetime
from datetime import datetime
from datetime import time
from datetime import date
from pywinauto.application import Application
from pyautogui import press
from pyautogui import sleep
from pyautogui import getWindowsWithTitle
from pyautogui import getAllTitles
from pynput import keyboard
from pynput.keyboard import Listener
from pynput.mouse import Listener
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from pynput.keyboard import Controller
from pynput import mouse
import array
from array import *
import numpy
from numpy import *

clckM = []
dragM = []
with open('C:\\Users\\USER\\PycharmProjects\\pythonProject\\PosMouse2.txt','r') as file:
    lnfile = len(file.readlines())
    # print(lnfile)
file.close()
with open('C:\\Users\\USER\\PycharmProjects\\pythonProject\\PosMouse2.txt','r') as file:
    for i in range(lnfile):
        lstline = file.readline()
        print(lstline)
        lnlstline = len(lstline)
        lnspc = lstline.find(' ') #нашли пробел
        lnpnt = lstline.find('.') #нашли точку
        lnxdg = lstline[0:lnspc]
        lnydg = lstline[lnspc+1:lnlstline]
        lst = lstline[0]
        clckM.append(lstline)
    print(clckM)
file.close()
for i in range(lnfile):
    data = clckM[i]
    print(i, data)
    if data == str('Button.left.pressed\n'):
        a = clckM.index('Button.left.pressed\n',i)
        b = clckM.index('Button.left.relesed\n',i)
        c = b-a
        print(a, b, c)
        if c == 6:
            ax0 = int(clckM[a+1])
            ax1 = int(clckM[a+4])
            ay0 = int(clckM[a+2])
            ay1 = int(clckM[a+5])
            txy = float(clckM[a+3])
        print(ax0, ax1, ay0, ay1, txy)
        print((abs(ax0-ax1)))
        if (abs(ax0-ax1)<2) and (abs(ay0-ay1)<2) and (txy<0.3):
            print('это клик')
            sleep(2)
            # pyautogui.leftClick()
            print('LeftClick')
            pyautogui.click(ax1, ay1, duration=2)
        else:
            print('это drag')
            pyautogui.moveTo(ax0, ay0, duration=2)
            sleep(.1)
            pyautogui.dragTo(ax1, ay1, duration=2, button='left')
    else:
        print('мы здесь')




# a = clckM.index('Button.left.pressed\n',a+1)
# b = clckM.index('Button.left.relesed\n',b+1)
# print(a, b)