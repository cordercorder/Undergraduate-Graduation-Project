import os
import random

source_directory = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"
output_directory = "/data/rrjin/Graduation/data/bible-corpus/train_data"

random.seed(998244353)

combine_all_data_src = []
combine_all_data_tgt = []

for directory in os.listdir(source_directory):

    p = os.path.join(source_directory, directory)

    isv = set()
    tmp_src = []
    tmp_tgt = []

    cnt = 0

    for i, file in enumerate(os.listdir(p)):

        assert cnt < 2

        if not file.startswith("bible_tokenize"):
            continue

        with open(os.path.join(p, file)) as f:
            data = f.read().split("\n")

        if file.endswith("en"):
            if cnt == 0:
                for j, sentence in enumerate(data):
                    if len(sentence) == 0:
                        isv.add(j)
                    else:
                        tmp_tgt.append(sentence)
            else:
                for j, sentence in enumerate(data):
                    if j in isv:
                        continue
                    tmp_tgt.append(sentence)
        else:
            idx = file.rfind(".") + 1
            if cnt == 0:
                for j, sentence in enumerate(data):
                    if len(sentence) == 0:
                        isv.add(j)
                    else:
                        s = file[idx:] + " " + sentence
                        tmp_src.append(s)
            else:
                for j, sentence in enumerate(data):
                    if j in isv:
                        continue
                    s = file[idx:] + " " + sentence
                    tmp_src.append(s)

        cnt += 1

    combine_all_data_src.extend(tmp_src)
    combine_all_data_tgt.extend(tmp_tgt)

# print(combine_all_data_src[:5])
# print(combine_all_data_tgt[:5])
# print(len(combine_all_data_tgt), len(combine_all_data_src))

combine_all_data = list(zip(combine_all_data_src, combine_all_data_tgt))

random.shuffle(combine_all_data)

# print(combine_all_data[:5])

combine_all_data_src = []
combine_all_data_tgt = []

for src, tgt in combine_all_data:
    combine_all_data_src.append(src)
    combine_all_data_tgt.append(tgt)

with open(os.path.join(output_directory, "merge_combine_all_data_src.txt"), "w") as f:
    f.write("\n".join(combine_all_data_src))

with open(os.path.join(output_directory, "merge_combine_all_data_tgt.txt"), "w") as f:
    f.write("\n".join(combine_all_data_tgt))