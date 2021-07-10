##Gives basic system functions
import sys
##   From this file      Import this function
from ImportModule import divide

## or from ImportModule
##    ImportModule.divide

print(divide(10,2))
print(__name__)

print(sys.path)
print(sys.modules)