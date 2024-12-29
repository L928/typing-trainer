

## 
# @file install_requirements.py
# @brief automativally do all steps to get requirements satisfied
# we don't use pip freeze or pipreqs because this is too slow for
# our purpose. We just want requirements silently be resolved. 

import importlib, os
from log import *

def do():
  for module in ["PyQt5"]:
    try:
      importlib.import_module(module)
    except:
      print("module not installed:",module)
      cmd = "pip install "+module
      print(cmd)
      os.system(cmd)

