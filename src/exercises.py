

##
# @file exercises.py
# @brief A list of prepared exercises.

from collections import OrderedDict
#class Exercise(object):
  #def __init__(self, name, level = 1, symbols = "asdfjkl;", amount=10)
    
EXERCISES_CODED = OrderedDict()
e = EXERCISES_CODED


e[r"hands rest"]       = r"fj fj'\ !g! !h! fghj dk sl a; gh asdfg hjkl;'\ asdfghjkl;"
e[r"top row"]          = r"!qwertyuiop[]! ru ru[] ei wo qp ty [] qwert yuiop qwertyuiop[]"
e[r"bottom row"]       = r"!\zxcvbnm,./! vm c, x. z/\ bn \zxcvb bnm,./ \zxcvb bnm,./"
e[r"number row"]       = r"!`1234567890! - = 57 67 567 47-= 38 123456 67890-= 56 67  `129 `10 -= vm c, x. z/\ bn \zxcvb bnm,./ \zxcvb bnm,./"
e[r"middle row shift"] = r'ASDFGHJKL:"|'
e[r"bottom row shift"] = r"|ZXCVBNM<>?"
e[r"top row shift"]    = r"QWERTYUIOP{}"
e[r"number row shift"] = r"~!@#$%^&*()_+"


EXERCISES_DECODED = OrderedDict()

def decodeEcercises():
  major = 1
  for kategory, exerciseData in EXERCISES_CODED.items():
    minor = 1
    for exercise in exerciseData:
      #if exercise[0] == "!" and exercise[-1] == "!":
      #  exercise = exercise[1:-2]
      title = "{:>2d} {:s} {:>2d} ".format(major, kategory, minor )
      EXERCISES_DECODED[title] = exercise
      minor += 1
    major += 1
    
decodeEcercises()

if __name__ == "__main__":
  # run test
  from log import *
  if True:  
    logDict(EXERCISES_DECODED)
    pass
  
  if False:
    D = OrderedDict()
    D["c"]=1
    D["a"]=3
    D["b"]=2
    logDict(D)
    