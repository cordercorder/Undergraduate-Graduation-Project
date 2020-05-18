import os

parallel_text_path = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"

train_data_src_path = "/data/rrjin/Graduation/data/bible-corpus/train_data/train_combine_all_data_src_bpe.txt"
train_data_tgt_path = "/data/rrjin/Graduation/data/bible-corpus/train_data/train_combine_all_data_tgt_bpe.txt"

output_data_dir = "/data/rrjin/Graduation/data/bible-corpus/extract_lang_vec_data"

sentence_num = 200
count = {}
isv = set()

select_data_src = []
select_data_tgt = []

for directory in os.listdir(parallel_text_path):
    tmp = directory[:-4]
    language1, language2 = tmp.split("-")
    count[language1] = 0
    count[language2] = 0

count.pop("en")

with open(train_data_src_path) as f:
    train_data_src = f.read().split("\n")


with open(train_data_tgt_path) as f:
    train_data_tgt = f.read().split("\n")

assert len(train_data_src) == len(train_data_tgt)

length = len(train_data_src)


def check():
    for value in count.values():
        if value != sentence_num:
            return False
    return True


for i in range(len(train_data_src)):
    words = train_data_src[i].split()
    language = words[0]
    num = count.get(language)

    if num == sentence_num:
        continue
    count[language] = num + 1

    select_data_src.append(train_data_src[i])
    select_data_tgt.append(train_data_tgt[i])

if check():
    with open(os.path.join(output_data_dir, "data_src.txt"), "w") as f:
        f.write("\n".join(select_data_src))

    with open(os.path.join(output_data_dir, "data_tgt.txt"), "w") as f:
        f.write("\n".join(select_data_tgt))
else:
    print("Error!")