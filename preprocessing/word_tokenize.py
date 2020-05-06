from nltk import word_tokenize
import os

source_directory = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"

for directory in os.listdir(source_directory):
    p = os.path.join(source_directory, directory)

    for file in os.listdir(p):
        con = []
        file_name_prefix = "bible_tokenize"

        with open(os.path.join(p, file)) as f:
            data = f.read().split("\n")
            for sentence in data:
                tok_sentence_list = word_tokenize(sentence)
                tok_sentence = " ".join(tok_sentence_list)
                con.append(tok_sentence)
        print(file_name_prefix + file[11:])
        with open(os.path.join(p, file_name_prefix + file[11:]), "w") as f:
            f.write("\n".join(con))