

import inspect

total_num_of_tests = 0
failed_tests = 0
def isEqual(a,b):
  return a == b
  
def isNotEqual(a,b):
  return a != b
  

def test(name,a,b, compare = isEqual): # expect a equal b
  global total_num_of_tests
  global failed_tests
  total_num_of_tests += 1
  result = compare(a,b)
  if result == True:
    print("OK    ",name) #str(a)," == ",str(b))
  else:
    failed_tests += 1
    print("ERROR ",name) #str(a)," != ",str(b))
    print("a = '"+repr(a)+"'")
    print("b = '"+repr(b)+"'")
    
    callerframerecord = inspect.stack()[2]    # 0 represents this line
                                              # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print("  line",info.lineno, "of", info.filename) 
    print("  in function",info.function)
    print("  a:",repr(a))
    print("  b:",repr(b))    

# expect equal    
def E(name,a,b):
  return test(name,a,b,compare = isEqual)
  
# expect not equal
def N(name,a,b):
  return test(name,a,b,compare = isNotEqual)
  
# expect true
def T(name, x):
  return test(name,x,True,compare = isEqual)
  
# expect false
def F(name, x):
  return test(name,x,False,compare = isEqual)
  
def printSummary():
  global total_num_of_tests
  global failed_tests
  print("="*100)
  print("number of tests: ",total_num_of_tests)
  print("failed tests: ",failed_tests) 
  print("="*100)
  
  
  