

##
# @# file filter.py
# @brief This is used to log which files are prodcessed
# by doxygen, to debug the doxygen run.
# set
# INPUT_FILTER           = filter.py
# in doxygen_config.txt to use it.
import os,sys

with open("log.txt","a") as f:
  f.write(os.path.relpath(sys.argv[1]+"\n"))
print(sys.argv[1])

