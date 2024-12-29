

##
# @file functions.py
# @brief Some static functions used in this application.
import os, random, textwrap, traceback
from log import *
ASCII_CHARS = '"'+r"!\n #$%&'()*+,–-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
RANDOM_REPETITIONS_ON_ERROR = 5
DIRECT_REPETITIONS_ON_ERROR = 3

INSERT_THRESHOLD = 0.9 # a large number makes it more likely that extra training letters come
        # at the end


TEST_PARAGRAPH="""Suspendisse montes mus tellus gravida
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

def Q(s):
  return "'"+s+"'"

def compareText(a,b):
  stringMap = ''
  la = len(a)
  lb = len(b)
  # returns a string map of differences
  for x in range(max(la,lb)):

    if x >= la:
      stringMap+=("a")
    elif x >= lb:
      stringMap+=("b")
    elif a[x] != b[x]:
      stringMap+=("x")
    else:
      stringMap+=(".") # means: equal
  return stringMap
  
          
def cntDnToZero(var):
  if var < 1:
    return 0
  return var-1
  

## @param s string to search
## @param pos position to start the relative search
## @param N how many spaces to skip, see explaination
def findSpace(s,pos,N):

  """Finde the N-th space character relative to a given position
  in a string.
  N = 0 is the closest to the right, or the space
  at the given position.
  N > 0 is the N-th space after the space of N=0.
  N < 0 is the abs(N)-th space to the left.

  say dist is an integer N from -inf to + inf
  we return the string index that correspond to the Nth space 
  relative to the current cursor position,
  as illustrated in this figure:                         c
                           |
  [X][X][ ][X][X][ ][X][X][ ][X][X][ ][X][X][ ][X][X][ ][X][X]
         |        |     |  |        |        |        |       
  N=    -2       -1     C  0        1        2        3
                                           
  c = current cursor position, the text under the cursor is a space
  C = current cursor position, the text under the cursor is not a space
  
  [X] = any non-sace character
  [ ] = a space character
  
  note: 
    if N is < 0 and the cursor is not on a space, the N value is off by one,
    because of the order of evaulation and counting in the used algorithm
  
  """
  #pos #= #len(self._typedText)-1
  if N < 0:
    n = -1
    if s[pos] != " ":
      N += 1 # see note
  else:
    n = 1

  while True:
    if pos == 0:
      return 0
    
    if pos == len(s)-1:
      return pos
      
    if s[pos] == " ":
      if N == 0:
        return pos   
        
      N -= n
      
    pos += n

def generateExercise(symbols, count):
  text = ""
  for x in range(count): # symbols:
    word = shuffleString(symbols)
    text += word + " "
  text = text[:-1] # removwe last space
  return text

def indexOfFirstDifference(refText,text2):
  #if len(text2) < len(refText):
  i = 0
  L = len(refText)
  for i in range(len(text2)): #min(len(text1),len(text2))):
    if i>=L:
      return i

    if refText[i] != text2[i]:
      return i
      
  return len(text2)
  
  
def insertStringAt(s2,i,s):
  return s[:i] + s2 + s[i:]  
  
def isAscii(s):
  for c in s:
    if c not in ASCII_CHARS:
      log("not an ascii char:",repr(c))
      return False
  return True
  

def makeText(topic = "random_paragraphs", nr = None):
  for path,dirs, files in os.walk("../resources/text/"+topic):
    if nr == None:
      random.shuffle(files)
      nr = 0
    with open(os.path.join(path, files[nr])) as f:
      text = f.read()
      return text
    return("TEXT CREATION ERROR WITH FILE '"+files[0]+"'")

  
def randomText():
  try:
    import wikipedia
  except:
    log("Installing wikipedia...")
    os.system("pip install wikipedia")
    try:
      import wikipedia
    except:
      return "ERROR: Could not install wikipedia."

  # Loading a page summary sometimes fails, for sevral reasons.
  # For example, sometimes a network error, having musuated fovels, too long summary,
  # an artivle about wikipedia itself.
  # It is tried several times therefore, to get a proper text.
  for x in range(10):
    try:
      title = wikipedia.random()
      logVars("title")
      page = wikipedia.page(title)
      logVars("page")
      text = wikipedia.summary(page,sentences = 1)
      s = title = '\n' + text
      if not "ikipedia" in text:
        log("Not about wikipedia.")
        if isAscii(s):
          log("Text is ascii.")
          return s

    except Exception as e:
      print("exception occured:")
      print(traceback.format_exc())
      print(e)
    
  return "ERROR: Could not load a wikipedia page summary."

def reWrapText(text,lineWidth):
  unwrappedText = list(unwrapText(text))
  L=0 # current line length
  S=0 # last found space pos index
  #W=0 # pos. of last wrapped
  for i in range(len(unwrappedText)):
    L += 1 # count must start at 1, not at 0
    C = unwrappedText[i] # just abbrev
    if C == " ":
      S = i
    if L >= lineWidth:
      if S == 0: # force cut word
        unwrappedText[i] = unwrappedText[i]+"\n"
        # note: This is actually the application error, that a word is longer
        #   than the line. But grammatically correct word wrap is too complicated
        #   in relatio to this app, and using a lib would make a dependency,
        #   which w don't want.
      else:
        unwrappedText[S] = "\n"
      
      #W = S
      L = i - S + 1
      S = 0
      #  if S>0: # at least, the first space
      #    unwrappedText[S] = "\n"
      #    L -= S
      #S = i
    
  return ''.join(unwrappedText)  
    
## @param s The string to cleanup.    
def removeExtraSpace(s):
  """Make all whitespaces in string to single, by removing any extra."""
  while "  " in s:
    s = s.replace("  "," ")
  print("s = ",repr(s))
  return s
  
def shuffleString(s):
  l = list(s)
  random.shuffle(l)
  l = ''.join(l)
  return l

def unwrapText(text):
  unwrappedText = text.replace("\n"," ")
  unwrappedText = unwrappedText.replace("\r"," ")
  unwrappedText = unwrappedText.replace("\t"," ")
  for s in ".,:;!?":
    unwrappedText = unwrappedText.replace(s,s+" ")
  while "  " in unwrappedText:
    unwrappedText = unwrappedText.replace("  "," ")
  if unwrappedText[0] == ' ':
    unwrappedText = unwrappedText[1:]
  if unwrappedText[-1] == ' ':  
    unwrappedText = unwrappedText[:-1]
  return unwrappedText
  
def __test():
  import sys
  sys.path.append("__test")
  import test_framework as T
  import test_data as D
  
  # test compareText
  T.E("in case b is smaller",
    compareText("abcdefg","abCde"),
    "..x..bb")
   
  T.E("in case a is smaller",   
    compareText("abCde","abcdefg"),
    "..x..aa"
  )
  
  text = makeText(nr=1)
  T.E("fully equal", 
    compareText(text, text),
    "."*len(text)
  )  
    
  result = compareText(text, makeText(nr=0))
  T.T("not equal", "x" in result)

  # test generateExercise

  
  # test unwrapText
  if False:
    l = 0
    for i in unwrapText(D.text):
      print(i,end='')
      l += 1
      if l == 10:
        l = 0
        print("|")
  T.E("unwrapp text", D.unwrappedText,unwrapText(D.text))

  T.E("difference 1", indexOfFirstDifference(D.textA, D.textB), 20)
  T.E("difference 2", indexOfFirstDifference("abcde", "abCde"), 2)
  T.E("difference 3", indexOfFirstDifference("abc", "abcde"), 3)
  T.E("difference 4", indexOfFirstDifference("abc", "abCde"), 2)
  
  T.E("identical  1", indexOfFirstDifference(D.textA, D.textA), len(D.textA))
  T.E("identical  2", indexOfFirstDifference(D.textB, D.textB), len(D.textB))
  
  T.E("insertStringAt", insertStringAt("xyz",3,"abcdefgh"),"abcxyzdefgh")
  
  s = "abcdefghijklmnop"
  s2 = shuffleString(s)
  T.N("shuffled",s,s2)
  s2 = ''.join(sorted(s2))
  T.E("unshuffled",s,s2)
  
  # test findSpace
  s = "aaaaa aaaa aaaa aaaa aaaa aaaa aaaaa" # space at 5,10,15,20,25,30
  T.E("findSpace 1",findSpace(s,18,0),20)

  s="xxxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxxx"
  p=20
  T.E("findSpace 1",  findSpace( s, p, 10),len(s)-1)
  T.E("findSpace 2",  findSpace( s, p, 0), 20)
  T.E("findSpace 3",  findSpace( s, p, 1), 25)
  T.E("findSpace 4",  findSpace( s, p, 2), 30)
  T.E("findSpace 5",  findSpace( s, p, -1),15)
  T.E("findSpace 6",  findSpace( s, p, -2),10)
  T.E("findSpace 7",  findSpace( s, p, -10),0)
                                
  p=23                          
  T.E("findSpace 8",  findSpace( s, p, 10),len(s)-1)
  T.E("findSpace 9",  findSpace( s, p, 0), 25)
  T.E("findSpace 10", findSpace( s, p, 1), 30)
  T.E("findSpace 11", findSpace( s, p, -1),20)
  T.E("findSpace 12", findSpace( s, p, -2),15)
  T.E("findSpace 13", findSpace( s, p, -10),0)

  s = generateExercise("abc",3)
  T.E("generateExercise 1", len(s), 11)
  T.N("generateExercise 1", s, "abc abc abc")
  T.E("generateExercise 1", ''.join(sorted(s)), "  aaabbbccc")

if __name__ == "__main__":
  # running test
  __test()
  
  
  
