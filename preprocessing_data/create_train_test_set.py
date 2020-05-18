import os

directory = "/data/rrjin/Graduation/data/bible-corpus/train_data"

test_sentence_num = 2000

data_names = ["merge_combine_all_data_src_bpe.txt", "merge_combine_all_data_tgt_bpe.txt"]

p = [os.path.join(directory, item) for item in data_names]

src_data = []
tgt_data = []

for file in p:

    with open(file) as f:
        data = f.read().split("\n")

        if "src" in file:
            src_data.extend(data)
        else:
            tgt_data.extend(data)

with open(os.path.join(directory, "train_combine_all_data_src_bpe.txt"), "w") as f:
    f.write("\n".join(src_data[:-test_sentence_num]))

with open(os.path.join(directory, "train_combine_all_data_tgt_bpe.txt"), "w") as f:
    f.write("\n".join(tgt_data[:-test_sentence_num]))

with open(os.path.join(directory, "test_combine_all_data_src_bpe.txt"), "w") as f:
    f.write("\n".join(src_data[-test_sentence_num:]))

with open(os.path.join(directory, "test_combine_all_data_tgt_bpe.txt"), "w") as f:
    f.write("\n".join(tgt_data[-test_sentence_num:]))