# Environment variable 
import os
path   = os.environ.get("PATH", "")
user   = os.environ.get("USER", "unknown")
print(user)
editor = os.environ.get("EDITOR", "nano")    
print(editor)
val    = os.environ.get("SOMEVAR", "default")
os.environ["NAME"] = "VALUE"
