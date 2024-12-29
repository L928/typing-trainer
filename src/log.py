

## simple log functions
import json
import inspect

def log(*a,**k):
  print(*a,**k)
  
  
  
  
def logDict(d):
  if "name" in d:
    print("dict: ",name)
  else:
    print("dict:")
  print("~"*50)
  print(json.dumps(d,sort_keys=True, indent=2))
  
  

def logVar_(var_name):
    # Get the previous frame in the call stack
    frame = inspect.currentframe().f_back.f_back

    # Access local variables of the caller's frame
    local_vars = frame.f_locals
    #for x in local_vars[var_name]:
    #  print("=",x)
    #print(var_name+"="+
    print(" >"+var_name+"="+repr(local_vars.get(var_name)))
    # Return the variable if it exists
    # return local_vars.get(var_name, None)

def logVars(s):
  x = s.split(",")
  for q in x:
    logVar_(q)


def warn(*s):
  print("WARNING:",*s)
  
  