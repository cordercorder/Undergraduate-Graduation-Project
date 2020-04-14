import argparse
import os
import re

parser = argparse.ArgumentParser()

parser.add_argument("--source_directory", required=True, nargs="*")
parser.add_argument("--output_directory", required=True)
parser.add_argument("--output_file", required=True)

args, unknown = parser.parse_known_args()

src_data = []
tgt_data = []

for source in args.source_directory:
    for directory in os.listdir(source):
        with open(os.path.join(source, directory), encoding="utf-8") as f:
            data = f.read().split("\n")
        # print(directory, end=', ')

        idx = None
        if not directory.endswith("en"):
            idx = directory.rfind(".") + 1

        sentence_list = []
        for sentence in data:
            tmp = re.sub(r"[,.?;'\"`~:!]", " ", sentence)
            if len(tmp) == 0:
                continue
            if idx:
                tmp = directory[idx:] + " " + tmp
            sentence_list.append(tmp)

        if idx:
            src_data.extend(sentence_list)
        else:
            tgt_data.extend(sentence_list)

with open(os.path.join(args.output_directory, args.output_file + "_src.txt",), "w") as f:
    f.write("\n".join(src_data))

with open(os.path.join(args.output_directory, args.output_file + "_tgt.txt",), "w") as f:
    f.write("\n".join(tgt_data))