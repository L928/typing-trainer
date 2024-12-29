

##
# @file run_usability_tests.py
# @brief run the application usability tests

import os
for path,dirs,files in os.walk(os.path.dirname(__file__)):
  for f in files:
    if f.endswith("__usability_test.py"):
      uri = os.path.abspath(os.path.join(path,f))
      print(uri)
      os.system(uri)
      