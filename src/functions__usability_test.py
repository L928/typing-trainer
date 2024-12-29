

##
# @file functions.py
# @brief Some static functions used in this application.
import functions as F

while True:

  print(F.randomText())
  i = input("Input x to end, otherwise press enter to repeat.")
  if i.lower().startswith("x"):
    break
  