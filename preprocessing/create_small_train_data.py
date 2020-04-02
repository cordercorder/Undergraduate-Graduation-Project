import os

source = "/data/rrjin/Graduation/data/bible-corpus/train_data"

src = "train_src_zh.txt"
tgt = "train_tgt_en.txt"

with open(os.path.join(source, src)) as f:
    tmp = f.read().split("\n")

with open(os.path.join(source, "part_of_train_src_zh.txt"), "w") as f:
    f.write("\n".join(tmp[:1000]))

with open(os.path.join(source, tgt)) as f:
    tmp = f.read().split("\n")

with open(os.path.join(source, "part_of_train_tgt_en.txt"), "w") as f:
    f.write("\n".join(tmp[:1000]))
