

##
# @file qt_text_edit_x.py
# @brief QTextEdit with app specific extensions

from qt import *
from log import *

# a QTextEdit with some extensions specific for this app
class QtTextEditX(QW.QTextEdit):
  """ a QTextEdit with some extensions specific for this app """
  fontsize = 16
  def __init__(self, content):
    super().__init__(content) #content)
    self.setLineWrapMode(QW.QTextEdit.WidgetWidth) #NoWrap)
    
  # this is currentl8y not in use, but kept in case it turns out
  # to be better to mousewheelzoom both text windows independently
  # the xx_ makes it happen that wheelEvent isn't overridden by this
  def xwheelEvent(self,event):
    
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

  ## @param start_pos Index of first marked character.
  ## @param end_pos Index _after_ last marked character.  
  ## @param color RGB Value for the color.
  def highlightText(self, start_pos, end_pos, color = (230,255,230) ):
    """
    Add backgroud color to a text segment.
    """
    cursor = self.textCursor()
    cursor.setPosition(start_pos)
    cursor.setPosition(end_pos, QG.QTextCursor.KeepAnchor)
    format = QG. QTextCharFormat()
    format.setBackground(QG.QColor(color[0],color[1],color[2]))
    cursor.mergeCharFormat(format)

  ## @param text Text to compare to.
  def markDiff(self, text):
    """
    Mark identical text beginning green, errors red, rest white.
    """
    # remove previous marking
    s = self.toPlainText()
    self.clear()
    self.setPlainText(s)  
    
    # The highlightText function needs the index AFTER the text to highlight,
    # so we pass i+1, see below. However, if no text has to be marked,
    # i+1 would be 0+1, so one character was marked.
    # This is avoided by aborting the marking if the given text length is 0.
    if len(text) == 0:
      return
      
    OK_COLOR = (180,255,180)
    ERROR_COLOR = (255,180,180)
    ref = self.toPlainText()
    logVars("ref")
    logVars("text")
    print("len(ref)",len(ref))
    print("len(text)",len(text))
    commonLength = min(len(ref), len(text))
    logVars("commonLength")
    i = 0 # see note
    for i in range(commonLength):
      #print(i,text[i],ref[i])
      if text[i] != ref[i]:  
        self.highlightText(0,i,color = OK_COLOR)
        self.highlightText(i,commonLength,color = ERROR_COLOR)
        return # first difference only

    self.highlightText(0,i+1,color = OK_COLOR)

# note: in case commonLength is 0, the for is never exec,
# so set i to 0 inthat case
