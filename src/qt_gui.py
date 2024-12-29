

##
# @file qt_gui.py
# @brief qt based app gui

""" the application gui file """
import os, random, sys
from qt import *
from log import *
import functions as F
import qt_text_edit_x as QTX
import qt_wizard as W


def c():
  return random.randint(0,255)
  
class AppWidget(QW.QWidget):
  """The application gui"""
  def __init__(self, appObj, testMode = False):
    super().__init__()
    self.A = appObj
    self.fontsize = 16
    self.initUI(testMode)
    self.setGeometry(50,50,1000,800)
    self.currentExercise = None
    self.alreadyNotifiedFinish = False
    
  def initUI(self, testMode):
    if testMode:
      print("-"*100)
      print(os.getcwd())
      fileName = "oneliner"
      
      with open("../resources/test/"+fileName+".txt") as f:
        self.A.referredText(f.read())
    else:
      self.A.referredText(F.makeText())

    self.setWindowTitle("Typing Trainer")
    self.mainLayout = QW.QVBoxLayout(self)
    self.buttonLayout = QW.QHBoxLayout()
    self.mainLayout.addLayout(self.buttonLayout)
    #self.layout.setContentsMargins(1,1,1,1)
    #self.layout.setSpacing(1)
    
    # load button
    self.loadButton = QW.QPushButton("Load exercise")
    self.buttonLayout.addWidget(self.loadButton)
    self.loadButton.pressed.connect(self.onLoadClick)     
    
    # wizard
    self.wizardButton = QW.QPushButton("Wizard")
    self.buttonLayout.addWidget(self.wizardButton)
    self.wizardButton.pressed.connect(self.onWizardClick)     
    
    # random button
    self.randomButton = QW.QPushButton("Random Text")
    self.buttonLayout.addWidget(self.randomButton)
    self.randomButton.pressed.connect(self.onRandomTextClick)  

    
    # test window with the text to type
    self.sourceTextWindow = QTX.QtTextEditX(self.A.referredText())
    self.mainLayout.addWidget(self.sourceTextWindow)
    self.sourceTextWindow.setReadOnly(True)
    # window to type text into
    self.workTextWindow = QTX.QtTextEditX("")
    self.mainLayout.addWidget(self.workTextWindow)
    self.workTextWindow.textChanged.connect(self.workTextChanged)
    self.workTextWindow.setFocus()
    
  #def markProgress(self):
  #  text = self.workTextWindow.toPlainText()
  #  refText = self.sourceTextWindow.toPlainText()
  #  I = F.indexOfFirstDifference(refText, text)
  #  
  #  self.sourceTextWindow.clear()
  #  self.sourceTextWindow.setHtml(refText)
  #  self.sourceTextWindow.highlight_text(0,I)
  #  
  #  self.sourceTextWindow.highlight_text(I,
  #    min(len(text),len(refText)),(255,100,100)
  #  )  
    
  def updateTextWindows(self):
    """Insert text, put cursor to end, mark progress and errors.""" 
    self.workTextWindow.blockSignals(True)    
    self.workTextWindow.setPlainText(self.A.typedText())
    cursor = self.workTextWindow.textCursor()
    cursor.movePosition(cursor.End) 
    self.workTextWindow.setTextCursor(cursor)
    self.workTextWindow.blockSignals(False)

    self.sourceTextWindow.setPlainText(self.A.referredText())
    self.sourceTextWindow.markDiff(
      self.A.typedText()
    )

  def workTextChanged(self):
    enteredText = self.workTextWindow.toPlainText()
    textBefore = self.A.typedText()
    logVars("textBefore")
    logVars("enteredText")
    self.A.typedText(enteredText)    

    numCharsEntered = len(enteredText) - len(textBefore) # negativ = deleted
    print("numCharsEntered=",numCharsEntered)
    if numCharsEntered == 0:
      pass
      
    elif numCharsEntered < 0:
      print("DELETED...")
      if enteredText == "":
        print("SETTING TYPED TEXT SET To NOTHING !!!")
        self.A.typedText("")
        print("TYPED TEXT SET To NOTHING !!!")
      else:
        self.A.typedText(enteredText)

    # block copy paste action, since it would lead to 
    # undefined behaviour      
    elif numCharsEntered > 1:
      self.A.typedText(textBefore) 
      
    else:  
      refBefore = self.A.referredText() #sourceTextWindow.toPlainText()
      self.A.handleMistyping()
      refAfter = self.A.referredText() #self.sourceTextWindow.toPlainText()
      if refBefore != refAfter:
        self.showPopup("Mistyped ! Added extra exercise")

    self.updateTextWindows()    
    
    if self.A.isFinished():
      if self.alreadyNotifiedFinish == False:
        self.alreadyNotifiedFinish = True
        what = self.currentExercise
        if what == None:
          what = ""
        self.showPopup("Fininshed "+what+" !")
    else:
      self.alreadyNotifiedFinish = False    
  
  def showPopup(self,s,t=3000):
    msg = QW.QMessageBox(self)
    msg.setIcon(QW.QMessageBox.Information)
    msg.setWindowTitle("Info")
    msg.setText(s)
    
    if t == 0:
      msg.exec_()
    else:
      msg.show()
      QC.QTimer.singleShot(t, msg.close)
      
  def wheelEvent(self,event):
    modifiers = QW.QApplication.keyboardModifiers()
    if modifiers == QC.Qt.ControlModifier:
      # text zoom
      if event.angleDelta().y() > 0:
        self.fontsize+=1
      else:
        self.fontsize-=1
      self.fontsize = min(self.fontsize,40)
      self.fontsize = max(self.fontsize,8)
      self.setFont(QG.QFont('Courier New', self.fontsize))        
    self.sourceTextWindow.setFont(QG.QFont('Courier New', self.fontsize))  
    self.workTextWindow.setFont(QG.QFont('Courier New', self.fontsize))  
    
    
  def newText(self, text):
    self.A.referredText(text) 
    self.A.typedText("")
    self.updateTextWindows()
    self.workTextWindow.setFocus()
    self.A._toRetype = ''
    self.alreadyNotifiedFinish = False
    
  def onRandomTextClick(self):

    """Use wikipedia ramdon page to create text from it's summary.
    To do this, we first install the wikipedia module if it is not 
    already isntalled.  
    """
    text = F.randomText()
    if text.startswith("ERROR: "):
      self.showPopup(text)
    else:
      self.newText(text)
   
  def onLoadClick(self):
    text = ''
    cwd = os.getcwd()
    fileInfo = QW.QFileDialog.getOpenFileName(self, 'open config file', 
      cwd+"/../resources/exercises", "text files (*.txt)")
    
    if fileInfo[0] != "":
      self.currentExercise = os.path.basename(fileInfo[0])
      with open(fileInfo[0]) as f:
        for l in f:
          if l.startswith("#"):
            continue
          text+=l
    self.newText(text) 
    
  def onWizardClick(self):
    w = W.Wizard({
        "enter symbols to exercise":"fj",
        "enter how many":20
      }, title = "Exercise Generator Wizard",
      helpText = """
This wizard will create a text to exercise typing
the given symbols.
      """
    )
    
    
    if w.exec_() == QW.QDialog.Accepted:
      data = w.getData()
      logDict(data)
      
      text = F.generateExercise(
        data["enter symbols to exercise"],
        data["enter how many"]
      )
      self.newText(text)
      
    else:
      pass
      