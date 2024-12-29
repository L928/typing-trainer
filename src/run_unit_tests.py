
##
# @file run_unit_tests.py
# @brief run the application unit tests
import os, sys
import functions
import app__test

# set path to src as workdir
print("cwd:",os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# test the test framework
print("checking test framework")
print("-"*100)
sys.path.append("__test") # see note
# note: This is to make the behaviour of this script independent
#   of the work dir where it was run from.
import test_framework as T
T.E("test E",True,True)
T.N("test N",True,False)
T.T("test T",True)
T.F("test F",False)


print("running functions.__test()")
print("-"*100)
functions.__test()

print("running app__test.__test()")
print("-"*100)
app__test.__test()

T.printSummary()