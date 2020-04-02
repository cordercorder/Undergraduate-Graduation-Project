import re
import os

source = "/data/rrjin/Graduation/data/bible-corpus/parallel_text/en-fr.txt"
output = "/data/rrjin/Graduation/data/bible-corpus/train_data"

train_src_fr_path = os.path.join(source, "bible-uedin.en-fr.fr")
train_tgt_en_path = os.path.join(source, "bible-uedin.en-fr.en")

for item in [(train_src_fr_path, "train_src_fr.txt"), (train_tgt_en_path, "train_tgt_en.txt")]:
    train_data = []
    with open(item[0]) as f:
        data = f.read()
        for sentence in data.split("\n"):
            sentence = re.sub(r"[,.?;'\"`~:!]", r" ", sentence)
            train_data.append(sentence)
            # print(sentence)


    with open(os.path.join(output, item[1]), "w") as f:
        f.write("\n".join(train_data))