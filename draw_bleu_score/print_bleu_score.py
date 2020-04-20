import subprocess
import os

source_dir = "/data/rrjin/Graduation/final_tests_combine_fr_de_lstm"

suf = ["1250", "2500", "3750"]
prefix = "repeat_1_result_"

for i in range(10):
    f = [prefix + str(i) + "_" + s + ".txt" for s in suf]
    for file_name in f:

        command = "tail -n 1 " + os.path.join(source_dir, file_name)
        # print(command)
        subprocess.call(command, shell=True)