import os

parallel_dir = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"
merge_data_path = "/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_src_bpe.txt"

language_set = set()

for directory in os.listdir(parallel_dir):
    p = os.path.join(parallel_dir, directory)
    for file in os.listdir(p):
        idx = file.rfind(".") + 1
        language_set.add(file[idx:])

language_set.remove("en")

with open(merge_data_path) as f:
    data = f.read().split("\n")
    for i, sentence in enumerate(data):
        words = sentence.split()
        if words[0] not in language_set:
            print("Error!")
            print(sentence)
            print("{}th row!".format(i))

print("ok")