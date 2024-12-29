
##
# @file run.py
# @brief This creates the documentation.
import os, datetime, sys
with open("log.txt","w") as f:
  f.write("")
os.system("doxygen doxygen_config.txt")
os.system("pause")
