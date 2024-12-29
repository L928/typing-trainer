

##
# @file qt_wizard.py
# @brief app specific input dialog

from qt import *

STYLE_OK = "background color: rgb(230,255,230); color: rgb(0,100,0)"
STYLE_ERROR = "background: rgb(255,200,200)"
STYLE_OK = "color: rgb(0,150,0)"

# a QTextEdit with some extensions specific for this app
class Wizard(QW.QDialog ):
  """ a QWidget for this app to create a custom exercise."""
  fontsize = 16
  def __init__(self, data, title = "Wizard", helpText = "No help text."):
    super().__init__()
    self.myLayout = QW.QGridLayout(self)    
    self._data = data
    self.valDialogs = dict()

    self.myLayout.addWidget(QW.QLabel(helpText),0,0,1,0)
    self.setWindowTitle(title)  

    line = 1
    for k,v in data.items():
      line += 1
      l = QW.QLabel(k)
      w = QW.QLineEdit(str(v))
      w.setStyleSheet(STYLE_OK)
      w.textChanged.connect(self.validate)
      self.myLayout.addWidget(w,line,1)
      self.myLayout.addWidget(l,line,0)
      self.valDialogs[k] = w
    
    # Button box for OK and Cancel buttons
    button_box = QW.QDialogButtonBox(QW.QDialogButtonBox.Ok | QW.QDialogButtonBox.Cancel, self)
    button_box.accepted.connect(self.onOk)
    button_box.rejected.connect(self.reject)

    self.myLayout.addWidget(button_box)    
    #self.valDialogs[k] = w
    #self.setModal(True)
    
  def validate(self):
    failed = False
    for k,v in self._data.items():
      print("k:",k,repr(v))
      valInType = self.toType(self.valDialogs[k].text(), self._data[k])
      if valInType == None:
        #print("validation failed")
        self.valDialogs[k].setStyleSheet(STYLE_ERROR) #"color: rgb(255,0,0)") #STYLE_ERROR)
        failed = True
      else:
        self.valDialogs[k].setStyleSheet(STYLE_OK)
        self._data[k] = valInType
    return not failed

  def onOk(self):
    if self.validate():
      self.accept()
    
  def getData(self):
    for k,v in self._data.items():
      self._data[k] = self.toType(self.valDialogs[k].text(), self._data[k])
      
    return self._data

  def toType(self, val, refVal):
    #print("types:", type(val), type(refVal))
    result = None
    try:
      if type(refVal) == int:
        #print("is int")
        result = int(val)
      elif type(refVal) == float:
        #print("is float")
        result = float(val)
      elif type(refVal) == str:
        if val == "":
          result = None
        else:
          result = str(val)
      else:
        #print("is other")
        result = repr(val)
    except ValueError:
      #print("exception")
      pass #result = None #return None
    
    #print("result",result)
    return result

  def run(self):
    self.show()
    
