import argparse
import os
import re
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--source_directory", required=True, nargs="*")
parser.add_argument("--output_directory", required=True)
parser.add_argument("--output_file", required=True)

args, unknown = parser.parse_known_args()

src_data = []
tgt_data = []

for i, source in enumerate(args.source_directory):
    src_data.append([])
    tgt_data.append([])
    for directory in os.listdir(source):
        with open(os.path.join(source, directory), encoding="utf-8") as f:
            data = f.read().split("\n")
        # print(directory, end=', ')

        idx = None
        if not directory.endswith("en"):
            idx = directory.rfind(".") + 1

        sentence_list = []
        for sentence in data:
            tmp = re.sub(r"[,.?;'\"`~:!。，？、．]", " ", sentence)
            if len(tmp) == 0:
                continue
            if idx:
                tmp = directory[idx:] + " " + tmp
            sentence_list.append(tmp)

        if idx:
            src_data[i].extend(sentence_list)
        else:
            tgt_data[i].extend(sentence_list)

for i in range(len(src_data)):
    if len(src_data[i]) != len(tgt_data[i]):
        print("The size of src_data and tgt_data is different!")
        sys.exit(1)

min_len = min([len(item) for item in src_data])

f_src = open(os.path.join(args.output_directory, args.output_file + "_src.txt",), "w")
f_tgt = open(os.path.join(args.output_directory, args.output_file + "_tgt.txt",), "w")

for i in range(min_len):
    for j in range(len(src_data)):
        f_src.writelines(src_data[j][i] + "\n")
        f_tgt.writelines(tgt_data[j][i] + "\n")

f_src.close()
f_tgt.close()
print("Done!")