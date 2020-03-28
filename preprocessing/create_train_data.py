import re
import os

source = "/data/rrjin/Graduation/data/bible-corpus/parallel_text/en-zh.txt"
output = "/data/rrjin/Graduation/data/bible-corpus/train_data"

train_src_zh_path = os.path.join(source, "bible-uedin.en-zh.zh")
train_tgt_en_path = os.path.join(source, "bible-uedin.en-zh.en")

train_src_zh = []
train_tgt_en = []

with open(train_src_zh_path) as f:
    train_src_data = f.read()
    for sentence in train_src_data.split("\n"):
        sentence = re.sub(r"[.!?、，。,．]", r" ", sentence)
        train_src_zh.append(sentence)
        # print(sentence)

with open(os.path.join(output, "train_src_zh.txt"), "w") as f:
    f.write("\n".join(train_src_zh))

with open(train_tgt_en_path) as f:
    train_tgt_data = f.read()
    for sentence in train_tgt_data.split("\n"):
        sentence = re.sub(r"[^a-zA-Z]", r" ", sentence)
        train_tgt_en.append(sentence)

with open(os.path.join(output, "train_tgt_en.txt"), "w") as f:
    f.write("\n".join(train_tgt_en))
