import os
import glob

source = "/data/rrjin/Graduation/data/bible-corpus/parallel_text/"

tmp = os.listdir(source)

print(type(tmp))
print(glob.glob(source + "en*"))