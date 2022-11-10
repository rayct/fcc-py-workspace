# freeCodeCamp - Scientific Computing with Python



# Strings and Lists

# words = 'His e-mail is q-lar@freecodecamp.org'
# pieces = words.split()
# parts = pieces[3].split('-')
# n = parts[1]
# print(n)


# Python Dictionaries

# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9
# print(dict)



# Dictionaries: Common Applications
# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))



# Python Dictionaries
# Key, Colon, Value
# dict = {"Fri": 20, "Thu": 6, "Sat": 1, "Sun": 9, "Mon": 8}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 10
# dict["Mon"] = 7
# print(dict)




# Dictionaries: Common Applications
# The get method for dictionaries
# Default value if key does not exist(and no traceback)
# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))




# Dictionaries and Loops
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])




# The Tuples Collection
# The comparison operators work with tuples and other sequences.
# If the first item is equal, python goes on to the next element, and son, until it finds elements that differ.
# d = dict()
# d['quincy'] = 1
# d['beau'] = 5
# d['kris'] = 9
# for (k,i) in d.items():
#     print(k, i)

#  Result:
# quincy 1
# beau 5
# kris 9



# Comparing and Sorting Tuples
# from collections import Counter

# lst = []
# for key, val in Counter.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# print(lst)


# a=input('Give new patient’s name:')
# b=int(input('Give new patient’s age:'))
# print(a, 'is' ,b, 'years old and a new patient!')

# first_number = input("First: ")
# second_number = input("Second: ")
# add = float(first_number) + int(second_number)
# print("Sum: " + str(add))


# RegEx in Python

# Search for lines that contain 'From'
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)


# Regular Expressions: Matching and Extracting Data

# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)


# Regular Expressions: Practical Applications
# What will search for a "$" in a regular expression?
# \$


# Networking with Python

# Networking: Write a Web Browser using Sockets
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt  HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()
# print(mysock)

# https://data.pr4e.org/romeo.txt
# https://www.ellatronix.com/notes.txt


# Networking: Text Processing
# UTF-8
# Find the Character set value:
# print(ord('%'))


# Networking: Using urllib in Python and some Web Scrapping
# 
#     print(fhand)


# Networking: Web Scraping with Python and html parsing, string parsing and split, RegX.


# Web Services: XML Schema
# What is XSD.?
# Answer: The W3C Schema Specification for XML

# Web Services: JSON

# import json
# data = '''
#   [
#     { "id" : "001",
#       "x" : "2",
#      "name" : "Quincy"
#     } ,
#     { "id" : "009",
#       "x" : "7",
#       "name" : "Mrugesh"
#     }
#   ]
# '''
# info = json.loads(data)
# print(info[1]['name'])


# Web Services: Service Oriented Approach

# Web Services: APIs = Application Program Interface

# Web Sevices: API Rate Limiting and Security

# Python Objects: Objects are one of the five standard data types

# Objects: A Simple Class
# class PartyAnimal:
#     x = 0
#     def party(self):
#         self.x = self.x + 2
#         print(self.x)
        
# an = PartyAnimal()
# an.Party()
# an.Party()


# Object Lifecycle
# Constructors
# Destructors
# class PartyAnimal:
#     x = 0
#     name = ''
#     def __init__(self, nam):
#         self.name = nam
#         print(self.name,'constructed')
#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)

# q = PartyAnimal('Quincy')
# m = PartyAnimal('Miya')

# q.party()
# m.party()
# q.party()
# Output:

# Quincy constructed
# Miya constructed
# Quincy party count 1
# Miya party count 1
# Quincy party count 2


# Objects: Inheritance
# What is inheritance in object-oriented programming?
# The ability to create a new class by extending an existing class.



daily = [3,1,2,4,5]
co = [daily,3,2,1]

co[1] =3
daily[3]= 1
co[2]= 2

print((sum(co[0])+co[1]+co[2]) % 5)































# ****************************************************************************************
# 5 Python GUI Frameworks for Developers
# ****************************************************************************************
# 5 Python GUI
# 1: PyQt5 GUI
# 2: TKinter GUI
# 3: Pyside2 GUI
# 4: wxPython GUI
# ****************************************************************************************
# ****************************************************************************************

# *********
# 1: PyQt5
# *********
# PyQt5 is a Graphical User Interface GUI Framework for python. It is one of the best, powerful and popular Python GUI Framework.
# PyQt is a binding of Qt5 C++ a gui framework for c++ developers.
# You can create program in pyqt5 using coding or a using qt designer a visual dialog that you can drag and drop UI widgets
# PyQt5 is a free Python bindings software open-source widget-toolkit Qt, implemented for cross-platform application development framework.
# In the free version, certain features may not be available but if your application is open source then you can use it under a free license.
# PyQt is available on Windows, MacOSX, Linux, Android iOS and Raspberry Pi.

# Installation
# pip install pyqt5

# from PyQt5.QtWidgets import QApplication,  QMainWindow
# import sys
# from PyQt5 import QtGui

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(300, 300, 500, 400)
#         self.setWindowTitle("PyQt5 Window")

#         self.show()

# App = QApplication(sys.argv)
# window = Window()
# sys.exit(App.exec())


# ***********
# 2: TKinter
# ***********
# Tkinter is the most popular programming package for graphical user interface or desktop apps.
# It is so named because of its simplicity.
# Tkinter is the combination of Tk and Python’s standard GUI framework.
# Tkinter It provides diverse widgets, such as labels, buttons, and text boxes used in a graphical user interface application.
# The Button control also called widgets are used to display buttons in developed application while the Canvas widget is used to draw shapes (lines, ovals, polygon…) in your application.
# It is a built in library for python.

# Installation
# It is a built in library in python, no need to install

# from tkinter import *

# class Root(Tk):
#     def __init__(self):
#         super(Root, self).__init__()
#         self.title("Python Tkinter First Window")
#         self.minsize(640, 400)
# root = Root()
# root.mainloop()



# **************************
# 3: Pyside2 (Qt For Python)
# **************************
# Qt for Python offers the official Python bindings for Qt (PySide2),
# enabling the use of its APIs in Python applications,
# and a binding generator tool (Shiboken2) which can be used to expose C++ projects into Python.
# Qt for Python is available under the LGPLv3/GPLv3 and the Qt commercial license.

# Installation
# pip install PySide2

# from PySide2.QtWidgets import QApplication,QWidget
# import sys
# import time

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Pyside2 Simple Application Expose C++ Apps")
#         self.setGeometry(300,300,500,400)


# myApp = QApplication(sys.argv)
# window = Window()
# window.show()
# myApp.exec_()
# sys.exit(0)



# ********
# 4: Kivy
# ********
# Kivy is Open source Python library for rapid development of applications that make use of innovative user interfaces, such as multi-touch apps.
# There are some features for kivy like.
# Kivy runs on Linux, Windows, OS X, Android, iOS, and Raspberry Pi.
# You can run the same code on all supported platforms.
# It can natively use most inputs, protocols and devices including WM_Touch, WM_Pen, Mac OS X Trackpad and Magic Mouse, Mtdev, Linux Kernel HID.
# Kivy is 100% free to use, under an MIT license, The toolkit is professionally developed, backed and used. 
# You can use it in a commercial product.
# The framework is stable and has a well documented API, plus a programming guide to help you get started.
# The graphics engine is built over OpenGL ES 2, using a modern and fast graphics pipeline.
# The toolkit comes with more than 20 widgets, all highly extensible.
# Many parts are written in C using Cython, and tested with regression tests.

# Installation
# Before installing Kivy, you need to install the following dependency and after that you can install kivy
# pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
# pip install Kivy

# from kivy.app import App
# from kivy.uix.button import Button

# class TestApp(App):
#     def build(self):
#         return Button(text = "Hello Kivy World from Ray Turner")


# TestApp().run()



# ************
# 5: wxPython
# ************
# wxPython is a cross-platform GUI toolkit for the Python programming language.
# It allows Python programmers to create programs with a robust, highly functional graphical user interface, simply and easily.
# It is implemented as a set of Python extension modules that wrap the GUI components of the popular wxWidgets cross platform library, which is written in C++.
# Like Python and wxWidgets, wxPython is Open Source, which means that it is free for anyone to use and the source code is available for anyone to look at and modify.
# And anyone can contribute fixes or enhancements to the project.
# wxPython is a cross-platform toolkit.
# This means that the same program will run on multiple platforms without modification. Currently Supported platforms are Microsoft Windows, Mac OS X and macOS, and Linux.

# Installation
# pip install wxPython

# import wx


# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(MyFrame, self).__init__(parent, title=title, size = (400,300))


#         self.panel = MyPanel(self)

# class MyPanel(wx.Panel):
#     def __init__(self, parent):
#         super(MyPanel, self).__init__(parent)


# class MyApp(wx.App):
#     def OnInit(self):
#         self.frame = MyFrame(parent=None, title="wxPython Window: By Ray Turner")
#         self.frame.Show()
#         return True

# app = MyApp()
# app.MainLoop()