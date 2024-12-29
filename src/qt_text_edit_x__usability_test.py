

##
# @file qt_text_edit_x__usability_test.py
# @brief usability test of q_text_edit_x
import functools, sys
from qt import *
import qt_text_edit_x

TESTS = {
  "colors":"Mark all words in the color except black.",
  "diff":"Mark text colors as inidcated by the text.",
  "error":"Mark text colors as inidcated by the text.",
  "paragraph":"Mark text colors as inidcated by the text.",
  "par.err":"Mark green up to before _RED_, and red uintil . and rest white.",
  "wrap":"Test word wrap",
  "clear":"Test clear text"
}

LOREM_YPSUM_TEXT_SHORT = """This part of
the paragraph, including the period, 
is green."""
LOREM_YPSUM_TEXT = LOREM_YPSUM_TEXT_SHORT+"""\
This part
has no color
at all."""

BIG_TEXT="""Suspendisse montes mus tellus gravida
, ultricies non. Vehicula vitae erat duis,
 maecenas aenean lobortis. Dui etiam non facilisi
 senectus conubia elit libero. Maecenas luctus inceptos
 placerat eget a senectus vivamus varius vulputate. 
 Eleifend habitant id sagittis pharetra vulputate;
 eu enim tristique. Dolor nisl congue nam praesent 
 viverra lectus venenatis. Facilisi pharetra pharetra 
 lacinia lacus ligula imperdiet sodales efficitur. 
 Donec justo est cubilia risus proin.
Fames placerat adipiscing porta interdum neque. 
Lorem vivamus himenaeos porta, enim ultrices duis. 
Venenatis lectus egestas magna curabitur penatibus lorem
 id nisl. Ipsum tortor hac proin massa elementum euismod
 metus. Eu euismod eget ornare pulvinar tincidunt lacus
 primis inceptos. Proin accumsan ornare condimentum penatibus 
 lobortis. In convallis fames nec in curae massa. Montes justo
 pellentesque mi, placerat condimentum blandit.
"""

NL = """
"""

class TestWidget(QW.QWidget):
  def __init__(self):
    super().__init__()
    #self.args = list()
    self.layout = QW.QVBoxLayout(self)

    docLabel = QW.QLabel(
      "This test is passed if:"+NL+\
      "1) It shows a test that is marked with green up to"\
      " the letter 'w', and from the letter 'o' to the end, it"\
      " should be marked red."+NL+\
      "2) If you press the 'make colorful'-button, it should show a text with color"\
      " names that are marked in that same color (excluding whitespace)."+NL+\
      "Except for black, which should not have a marking."\
    )
    docLabel.setWordWrap(True);
    self.layout.addWidget(docLabel)
    
    self.btns = list()
    x = 0
    for name, info in TESTS.items():
      self.addTest(name, info)
    
    self.t = qt_text_edit_x.QtTextEditX('')
    self.layout.addWidget(self.t)
    self.t.setPlainText("hello green red white world")
    self.t.markDiff("hello green xxx")
    
    #self.
   # self.t = t
    
  def addTest(self, name, info):
      #self.args.append(name)
      b=QW.QPushButton(name)
      layout = QW.QHBoxLayout()
      b.clicked.connect(lambda: self.buttonClicked(name[:]))
      layout.addWidget(b)
      layout.addWidget(QW.QLabel(info))
      self.layout.addLayout(layout)

  def buttonClicked(self, text):
    print(text)
    if text == "colors":  
      ##                        |5  |9    |15  |20    |27
      self.t.setPlainText("black red green blue yellow black")
      self.t.highlightText(6,9,color = (255,200,200)) # red
      self.t.highlightText(21,27,color = (255,255,100)) # tellow
      self.t.highlightText(10,15,color = (200,255,200)) # green
      self.t.highlightText(16,20,color = (200,200,255)) # blue
    
    if text == "diff":  
      self.t.setPlainText("greenWHITE")
      self.t.markDiff(    "green")
      
    if text == "error":  
      self.t.setPlainText("greenREDwhite")
      self.t.markDiff(    "green---")      
    if text == "paragraph":  
      self.t.setPlainText(LOREM_YPSUM_TEXT)
      self.t.markDiff(LOREM_YPSUM_TEXT_SHORT)
    if text == "par.err":  
      self.t.setPlainText(LOREM_YPSUM_TEXT.replace("green","_RED_"))
      self.t.markDiff(LOREM_YPSUM_TEXT_SHORT)
    if text == "wrap":  
      self.t.setPlainText(BIG_TEXT)
      self.t.markDiff(BIG_TEXT[0:int(len(BIG_TEXT)/2)])
    if text ==  "clear":
      self.t.clear()
    
if __name__ == '__main__':
  guiApp = QW.QApplication(sys.argv)
  window = TestWidget()
  window.show() 
  guiApp.exec()
