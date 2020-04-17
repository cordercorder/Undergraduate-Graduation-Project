import argparse
import os
import re

parser = argparse.ArgumentParser()

parser.add_argument("--source_directory", required=True)
parser.add_argument("--output_directory", required=True)
parser.add_argument("--output_file", required=True)

args, unknown = parser.parse_known_args()

src_data = []
tgt_data = []

for item in os.listdir(args.source_directory):
    idx = None
    if not item.endswith("en"):
        idx = item.rfind(".") + 1
    with open(os.path.join(args.source_directory, item), encoding="utf-8") as f:
        data = f.read().split("\n")
        for sentence in data:
            tmp = re.sub(r"[,.?;'\"`~:!]", " ", sentence)
            if len(tmp) == 0:
                continue
            if idx:
                src_data.append(item[idx:] + " " + tmp)
            else:
                tgt_data.append(tmp)

f_src = open(os.path.join(args.output_directory, args.output_file + "_src.txt",), "w")
f_src.write("\n".join(src_data))
f_src.close()

f_tgt = open(os.path.join(args.output_directory, args.output_file + "_tgt.txt",), "w")
f_tgt.write("\n".join(tgt_data))
f_tgt.close()