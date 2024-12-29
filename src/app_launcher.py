

##
# @file app_launcher.py
# @brief start the application in different ways (  window, no window, gui, test mode...)

import sys
import app
import qt_gui
from qt import *
import install_requirements
def exec_(testMode = False):
  install_requirements.do()

  A = app.App()
  appGui = QW.QApplication(sys.argv)
  appWindow = qt_gui.AppWidget(A, testMode = testMode)
  appWindow.show() 
  appGui.exec()

