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

from pynput.mouse import Button
from pynput.mouse import Controller

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# i = 1000
# while i >100:
#     print(i)
#     i /= 2

# with open('C:\\Users\\USER\\PycharmProjects\\pythonProjectGitHub\\PosMouse2.txt','r') as file:
#     lst = file.read()
#     print('read', lst)
# file.close()
#
# with open('C:\\Users\\USER\\PycharmProjects\\pythonProjectGitHub\\PosMouse2.txt','r') as file:
#     for line in file:
#         lst = file.read().split()
#         print('split', lst)
# file.close()
#
# with open('C:\\Users\\USER\\PycharmProjects\\pythonProjectGitHub\\PosMouse2.txt','r') as file:
#     lst = file.read().rsplit()
#     print('rsplit', lst)
# file.close()
#
# with open('C:\\Users\\USER\\PycharmProjects\\pythonProjectGitHub\\PosMouse2.txt','r') as file:
#     lst = file.read().splitlines()
#     print('splitlines', lst)
# file.close()
#
# with open('C:\\Users\\USER\\PycharmProjects\\pythonProjectGitHub\\PosMouse2.txt','r') as file:
#     lst = file.readlines()
#     print('readlines', lst)
# file.close()


with open('C:\\Users\\USER\\PycharmProjects\\pythonProject\\PosMouse2.txt','r') as file:
    lenfile =  len(file.readlines())
    print(lenfile)
file.close()


i = 1
with open('C:\\Users\\USER\\PycharmProjects\\pythonProject\\PosMouse2.txt','r') as file:
    # for line in file:
    for i in range(lenfile):
        print('шаг=', i)
        lst = file.readline()
        print('lst=', lst)
        ln = len(lst)
        print('длина строки=', ln)
        spc = lst.find(' ')
        pnt = lst.find('.')
        print(spc, pnt)
        ls = ln-spc
        lp = ln-pnt
        l1spc = lst[0:spc]
        # l2spc = lst[spc:-ln]
        l2spc = lst[spc:ln]
        print('x,y=', l1spc, l2spc)

        lpnt = lst[(pnt+1):(ln-1)]
        print('клавиша=', lpnt)

        lst1 = lst[0]
        print('входим в if;lst1=', lst1)
        if ln == 4:
            smb = lst[1]
            pyautogui.write(smb)
            print('это символ', smb)
        else:
            if lst1.isdigit():
                print(l1spc, l2spc)
                pyautogui.moveTo(int(l1spc), int(l2spc), duration=1)
                print('пошли на ', l1spc, l2spc)
            elif str(lpnt) == 'esc':
                sleep(.5)
                pyautogui.press('esc')
                print('Esc')
            elif str(lpnt) == 'rigth':
                sleep(.5)
                pyautogui.rightClick()
                print('RigthClick')
            elif str(lpnt) == 'left':
                sleep(0.5)
                pyautogui.leftClick()
                print('LeftClick')
            elif str(lpnt) == 'enter':
                sleep(.5)
                pyautogui.press('enter')
                print('Enter')
            elif str(lpnt) == 'tab':
                sleep(.5)
                pyautogui.press('tab')
                print('Enter')

        #     elif lst.find('enter'):
        #         keyboard.press(Key.enter)
        #     elif lst.find("'"):
        #         smb = lst[1]
        #         print('символ', smb)
        #         keyboard.press(smb)
        # else:
        #     print('это дата или буквы')
            # lst = file.readline()
        # lst = file.readline()
        # print('readline', lst)
        # lst = file.readline()
        # print('readline', lst)

file.close()



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# sleep(2)
# for i in range(12):
#     x,y = lst[i]
#     sleep(1)
#     # mouse.position = (x, y)
#     pyautogui.moveTo(x, y, duration=1)
#     sleep(0.5)
#     # print('Now we have moved it to {0}'.format(pyautogui.position))
#     print('Мы двинулись на ', x, y)


# with open('C:\\Users\\USER\\PycharmProjects\\pythonProjectGitHub\\PosMouse2.txt','r') as file:
#     lst = file.readlines()
#     del lst[0]
#     lst = [[float(n) for n in x.split()] for x in lst]
#     print(lst)
#     x,y = lst
#     sleep(1)
#     # mouse.position = (x, y)
#     pyautogui.moveTo(x, y, duration=1)
#     sleep(0.5)
#     # print('Now we have moved it to {0}'.format(pyautogui.position))
#     print('Мы двинулись на ', x, y)