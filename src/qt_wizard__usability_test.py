

##
# @file qt_wizard__usability_test.py
# @brief usability test of qt_wizard
import functools, sys
from qt import *
import qt_wizard

TESTS = {
  "wizard 1":"Popup a simple Wizard.",
  "wizard 2":"Popup a Wizard with instructions."
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
    self.args = list()
    self.layout = QW.QVBoxLayout(self)
    self.default = None
    docLabel = QW.QLabel(
      "Wizard Test."
    )
    docLabel.setWordWrap(True);
    self.layout.addWidget(docLabel)
    
    self.btns = list()
    x = 0
    for name, info in TESTS.items():
      self.addTest(name, info)

  def addTest(self, name, info):
      self.args.append(name)
      b=QW.QPushButton(name)
      b.setAutoDefault(True)
      layout = QW.QHBoxLayout()
      b.clicked.connect(lambda: self.buttonClicked(name[:]))
      layout.addWidget(b)
      layout.addWidget(QW.QLabel(info))
      self.layout.addLayout(layout)

  def buttonClicked(self, text):
    print(text)
    if text == "wizard 1":  
      w = qt_wizard.Wizard({
        "integer":1,
        "text":"hello world",
        "float":3.14,
        "list":[1, 2, 3],
        "set":{1, 2, 3},
        "tuple":(1, 2, 3)
      })
      
      if w.exec_() == QW.QDialog.Accepted:
        print("Dialog ok'd") 
      else:
        print("Dialog canceled")      

      data = w.getData()
      print(data)
      
    if text == "wizard 2":  
      w = qt_wizard.Wizard({
        "enter symbols to exercise":"",
        "enter how many":20
      }, title = "Exercise Generator Wizard",
      helpText = """
This wizard will create a text to exercise typing
the given symbols.
      """)
      
      if w.exec_() == QW.QDialog.Accepted:
        print("Dialog ok'd") 
      else:
        print("Dialog canceled")      

      data = w.getData()
      print(data)
      
  def onReturnKey(self):
    buttonClicked("wizard 2")
    
if __name__ == '__main__':
  guiApp = QW.QApplication(sys.argv)
  window = TestWidget()
  window.show() 
  guiApp.exec()
