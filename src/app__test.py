


##
# @file app__test.py
# @brief unit test of app.py

import os
import app

def __test():
  import sys
  sys.path.append("__test")
  import test_framework as T
  expect = T.E

  A = app.App()
  
  A.typedText("abc")
  A.referredText("abcdefg")
  expect("typed no error", A.getErrorPos(), None)
  expect("not finished", A.isFinished(), False)
  expect("whatWasWrong None None", A.whatWasWrong(),(None, None))
  
  A.typedText(A.typedText() + "X") # error typed
  expect("typed error", A.getErrorPos(), 3)
  expect("whatWasWrong X d", A.whatWasWrong(), ("X","d"))
  expect("not finished", A.isFinished(), False)
  
  A.typedText(A.referredText())
  expect("finished", A.isFinished(), True)
  expect("whatWasWrong None None", A.whatWasWrong(),(None, None))
  
  A.typedText(A.typedText() + "X") # typed beyond end
  expect("whatWasWrong X None", A.whatWasWrong(), ("X",None) )
  
  ##A.referredText("xxxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxxx")
  ##A.typedText(   "xxxxx xxxx xxxx xxxx-")
  ##expect("findSpace 1", findSpace(10),len(A.referredText())-1)
  ##expect("findSpace 2", findSpace(0), 20)
  ##expect("findSpace 3", findSpace(1), 25)
  ##expect("findSpace 4", findSpace(2), 30)
  ##expect("findSpace 5", findSpace(-1),15)
  ##expect("findSpace 6", findSpace(-2),10)
  ##expect("findSpace 7", findSpace(-10),0)
  ##
  ##A.referredText("xxxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxxx")
  ##A.typedText(   "xxxxx xxxx xxxx xxxx xx-")
  ##expect("findSpace 8", findSpace(10),len(A.referredText())-1)
  ##expect("findSpace 9", findSpace(0), 25)
  ##expect("findSpace 10",findSpace(1), 30)
  ##expect("findSpace 11",findSpace(-1),20)
  ##expect("findSpace 12",findSpace(-2),15)
  ##expect("findSpace 13",findSpace(-10),0)
 
if __name__ == "__main__":
  __test()
  
  