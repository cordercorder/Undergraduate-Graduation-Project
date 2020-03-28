import subprocess
import os

source = "/data/rrjin/Graduation/data/bible-corpus/parallel_text/"

for f in os.listdir(source):

    if f.endswith(".zip") and f.startswith("en"):

        command = "unzip -d " + source + f[:-4] + " " + source + f
        print(command)
        subprocess.call(command, shell=True)
