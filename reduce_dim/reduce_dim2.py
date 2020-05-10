import numpy as np
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def get_language_codes():
    language_codes_dir = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"
    langcode_set = set()
    for data_set in os.listdir(language_codes_dir):
        s = data_set[:-4]
        lang1, lang2 = s.split("-")
        langcode_set.add(lang1)
        langcode_set.add(lang2)
    langcode_set.remove("en")
    return list(langcode_set)


language_codes = get_language_codes()

source_dir = "/data/rrjin/Graduation/data/language_vector"
prefix = "combine_all_data_bpe_"

p = [os.path.join(source_dir, prefix + language + ".npy") for language in language_codes]

data = [np.load(item) for item in p]

# 2 Dimension
pca = PCA(n_components=2)
pca.fit(data)
data_new = pca.transform(data)
ax = plt.gca()
ax.scatter(data_new[:, 0], data_new[:, 1])

for i in range(len(data_new)):
    ax.text(data_new[i, 0], data_new[i, 1], language_codes[i])

ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.grid()
plt.savefig("reduce_dim_all_language_2.png")