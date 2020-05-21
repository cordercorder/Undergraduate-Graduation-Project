import numpy as np
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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
# source_dir = "/data/rrjin/Graduation/data/language_vector"
# source_dir = "/data/rrjin/Graduation/data/cell_states"
source_dir = "/data/rrjin/Graduation/data/hidden_states"

# prefix = "combine_all_data_bpe_"
# prefix = "cell_states_"
prefix = "hidden_states_"

p = [os.path.join(source_dir, prefix + language + ".npy") for language in language_codes]

data = [np.load(item) for item in p]

# 3 Dimension

pca = PCA(n_components=3)
pca.fit(data)
fig = plt.figure()
ax = fig.gca(projection="3d")
data_new = pca.transform(data)
# print(data_new)
ax.scatter(data_new[:, 0], data_new[:, 1], data_new[:, 2])

for i in range(len(data_new)):
    ax.text(data_new[i, 0], data_new[i, 1], data_new[i, 2], language_codes[i])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# plt.savefig("reduce_dim_all_language_3.png")
# plt.savefig("reduce_dim_all_language_cell_states_3.png")
plt.savefig("reduce_dim_all_language_hidden_states_3.png")