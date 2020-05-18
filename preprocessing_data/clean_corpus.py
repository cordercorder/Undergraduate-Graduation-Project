import os
import subprocess

source = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"

for directory in os.listdir(source):
    p = os.path.join(source, directory)
    for f in os.listdir(p):
        if f.find("-") == -1 or f.endswith(".xml"):
            delete_command = "rm " + os.path.join(p, f)
            print(delete_command, end=", ")
            if subprocess.call(delete_command, shell=True):
                print("delete failed")
            else:
                print("delete " + f)