import os
import pycountry

parallel_dir = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"
# data_path = "/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_src_bpe.txt"
data_path = "/data/rrjin/Graduation/data/bible-corpus/train_data/test_combine_all_data_src_bpe.txt"

language_dir = {}

for directory in os.listdir(parallel_dir):
    p = os.path.join(parallel_dir, directory)
    for file in os.listdir(p):
        idx = file.rfind(".") + 1
        language_dir[file[idx:]] = 0

language_dir.pop("en")

with open(data_path) as f:
    data = f.read().split("\n")
    for i, sentence in enumerate(data):
        words = sentence.split()
        if words[0] not in language_dir:
            print("Error1!")
            print(sentence)
            print("{}th row!".format(i))
        else:
            language_dir[words[0]] = language_dir.get(words[0]) + 1

for key, value in language_dir.items():
    if value == 0:
        print("Error2!")
        if len(key) == 2:
            lang = pycountry.languages.get(alpha_2 = key)
        else:
            lang = pycountry.languages.get(alpha_3 = key)
        print("language {}, language_id {}".format(lang, key))

print("ok")