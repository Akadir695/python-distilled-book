import module as mo
mo.a
mo.func()
s = mo.Someclass()
s.method()
"""
!if the module not found importError exception is raised
to import multiple module we use single import we use comma-separated list of names
import socket, os, re
! sometimes the local name used to refer to module is changed using the as qualifer to import
we can load specifi definations from module for example
we can use asterisk(*) to load all definations
"""
from module import func_tools, a
func_tools()
#! the behavior of global variable
a = 42
print(mo.a) # 27 modifying a in your script has no effect on the original in module.py.
from module import * 
