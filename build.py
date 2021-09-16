import glob
import os
headers = glob.glob("*.h")
sources = glob.glob("*.c")
buildScript = "gcc -Wall"

for h in headers:
    buildScript = buildScript + " " + h + " "
for c in sources:
    buildScript = buildScript + " " + c + " "

buildScript = buildScript + " -o build/Snowball.exe -lcsfml-graphics -lcsfml-audio -lcsfml-window -lcsfml-system -lsfml-graphics -lsfml-audio -lsfml-window -lsfml-system -llua5.1 -O2"

os.system(buildScript)