


##
# @file app.py
# @brief the main application implementation


## the app
import qt_gui
import functions as F
import exercises as E
from log import *

# note: SCHEDULE_THRESHOLD is the max. number of left added extra
#   symbols before new exrtras are added. This is to limit the amount
#   of to-retype.

class App(object):
  """The main application class.
  This class handles the interaction with the gui framework,
  and handles the application behaviour. 
  """
  
  def __init__(self):
    ## How many extra symbols added _before_ the mistyped word.
    self.EXTRA_BEFORE_NUMOF = 2  

    ## how many extra symbols added _after_ the mistyped word.
    self.EXTRA_AFTER_NUMOF = 2   
    
    ## How many extra symbols left to be re-typed before
    # adding new smbols on mistyping. This is to limit the number of
    # symbols added for retyping, if repeated mistyptings occur.
    self.SCHEDULE_THRESHOLD = 2  
    self._typedText = ""
    self._referredText = ""
    self._errIdx = None    ##< In the text string, the position of the first error, or None.

    self._numofToRetype = 0
    self._toRetype = ''
  def cursorPos(self):
    return len(self._typedText)-1
    
  def exercises(self):
    """Give a list of prepared exercises."""
    return E.EXERCISES
    
    
  def typedText(self, val = None):
    if val != None:
      self._typedText = val
      self._errIdx = None
    return self._typedText
    
  def referredText(self, val = None):
    if val != None:
      self._referredText = val
      self._errIdx = None
    return self._referredText
    
  def _getErrIdx(self):
    # caching the error pos to increase performance
    if self._errIdx == None:
      self._errIdx = F.indexOfFirstDifference(self._referredText, self._typedText)
    return self._errIdx
    
  def getErrorPos(self):
    """Returns the index of the first mistyped symbol."""
    I = self._getErrIdx()
    if I >= len (self._referredText):
      return None
    if I < len (self._typedText):
      return I
   
  def isFinished(self):
    """Returns true if all text was typed with no error."""
    #log("_typedText",self._typedText)
    #log("_referredText",self._referredText)
    I = self._getErrIdx()
    if I >= len(self._referredText): # finished
      return True
    return False
    
  def whatWasWrong(self):
    """Returns the symbol that was typed and the symbol that had to be typed."""
    if len(self._typedText) >  len(self._referredText):
      return self._typedText[-1],''

    if self.getErrorPos() == None:
      return (
        self._typedText[-1], 
        self._referredText[len(self._typedText)-1]
      )
      
    else:
      i = len(self._typedText)-1
      return self._typedText[i],self._referredText[i]

  def handleMistyping(self):
    """Handle the inserting of extra symbols to re-type on mistyping."""
    
    typed, expected = self.whatWasWrong()
    logVars("typed,expected")
    self._toRetype = ''.join(sorted(self._toRetype))
    log("self._toRetype",self._toRetype)    
    
    # After the exercise is finished, the user may type anything,
    # this doesn't give an error.
    if expected == '':
      return
      
    #log("typed '"+typed+"', expected '"+expected+"'")
    #log("self._toRetype=",self._toRetype)
    if typed == expected: # correclty typed
    
      # a correctly typed, previously mistyped symbol is removed from
      # the list of symbols to retype.
      if typed in self._toRetype:
        log("self._toRetype",self._toRetype) 
        print("typed=",typed)
        print("REMOVED ONE!")
        self._toRetype = self._toRetype.replace(typed,"",1) # remove one from the 'todo'
        log("self._toRetype",self._toRetype) 
      return 
    log("- error typed")
    
    # formatting keys are ignored for errors, we don't want to
    # change the formatting.
    for k in " \t\r\n":
      if (expected == k) or (typed == k):
        print("formatting key pressed")
        return 
    
    log("- not a space error")  
    # As long as there are more than SCHEDULE_THRESHOLD symbols to be 
    # re-typed, no extra symbols are inserted.
    log("CHECKING SCHEDULE_THRESHOLD")
    if self._toRetype.count(typed) > self.SCHEDULE_THRESHOLD:
      log("Already scheduled:",typed)
      return 
    log("- re-type not omitted")  


    log("INSERTING  ERROR")
    # what to add in case of mistype, before and after
    # the mistyped word, in random order
    S = expected+typed
    logVars("S")
    extraBefore=S*self.EXTRA_BEFORE_NUMOF #F.shuffleString(typed*self.EXTRA_BEFORE_NUMOF)
    extraAfter=S*self.EXTRA_AFTER_NUMOF #F.shuffleString(S*self.EXTRA_AFTER_NUMOF)
    log("extraBefore", extraBefore)
    log("extraAfter", extraAfter)
    self._toRetype+=extraBefore+extraAfter
    # insert it
    #i = self.cursorPos()

    s = self.referredText()
    p = self.cursorPos()
    
    # There is a special case: If a second error occurs at the beginning,
    # before the first space character, we dont want to insert extra
    # symbols BEFORE that, because then the previous already re-typed errors
    # had to be re-typed again.
    firstSpace = s.find(" ")
    if p<firstSpace:
      offset = 1
    else:
      offset = 0
    logVars("p,s,offset")
    p1 = F.findSpace(s, p, -1+offset)
    p2 = F.findSpace(s, p, 0+offset)

    # note: the text after the mistyped word must be entered first,
    #   because entering thext before moves the cousor position,
    #   and that would result iin a wrong foud space position !
    s = F.insertStringAt(" "+extraAfter+" ", p2, s)
    s = F.insertStringAt(" "+extraBefore+" ", p1, s)
    s = F.removeExtraSpace(s)
    if s[0] == " ": s = s[1:]
    #i += self.EXTRA_BEFORE_NUMOF
    self.referredText(s)


    #x spacePos = self.findSpace(0)
    #x s = F.insertStringAt(" "+extraAfter+" ", spacePos, self.referredText())
    #x if s[0] == " ": s = s[1:]
    #x self.referredText(s)



      
    # Since something was added, set the edit text back to
    # the point where everything was typed correctly.
    # This is for the user's convenience.
    errorPos = self.getErrorPos()
    if errorPos != None:
      log("ERROR POS",errorPos)
      self.typedText(self.referredText()[:errorPos])

      #self.typedText(s)
      
      # remove the mistyped text for convenience
      #errorPos = self.getErrorPos()
      #self.typedText(self.referredText()[:errorPos])
      
      
      #log("text after schedule:")
      #log(self.referredText())
      
    
    # remove the mistyped symbol from output
    ## self.typedText(self.typedText()[:-1])
    
    #self._lastWasMistyped = True

