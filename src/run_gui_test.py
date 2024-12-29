

##
# @file run_gui_test.py
# @brief run the application with cmd window in test mode

# system modules
import sys,traceback

# app. modules
import app, qt_gui
from qt import *


def run():
  A = app.App()
  appGui = QW.QApplication(sys.argv)
  appWindow = qt_gui.AppWidget(A, testMode = True)
  appWindow.show() 
  appGui.exec() 

try:
  run()

except Exception as e:
  print("exception occured:")
  print(traceback.format_exc())
  print(e)

