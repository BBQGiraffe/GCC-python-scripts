import sys
import os
from typing import TextIO
#creates a new .h and .c file for me :3
name = sys.argv[1].capitalize()
if os.path.exists(sys.argv[1] + ".c"):
    print("class " + name + " already exists silly boy!")
    exit()

headerguard = "" + name + "_H"

headertext = "#ifndef " + headerguard + "\n" + "#define " + headerguard + "\n\n\n#endif"
sourcetext = "#include \"" + sys.argv[1] + ".h\"\n"

headerfile = open(sys.argv[1] + ".h", "w+")
headerfile.write(headertext)
headerfile.close()




sourcefile = open(sys.argv[1] + ".c", "w+")
sourcefile.write(sourcetext)
sourcefile.close