import numpy as np
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

language_codes = ["de", "fr", "jap", "ru", "zh"]
source_dir = "/data/rrjin/Graduation/data/language_vector"
prefix = "combine_fr_de_zh_jap_ru__"

p = [os.path.join(source_dir, prefix + language + ".npy") for language in language_codes]

data = [np.load(item) for item in p]

# 3 Dimension

# pca = PCA(n_components=3)
# pca.fit(data)
# fig = plt.figure()
# ax = fig.gca(projection="3d")
# data_new = pca.transform(data)
# print(data_new)
# ax.scatter(data_new[:, 0], data_new[:, 1], data_new[:, 2])
#
# for i in range(len(data_new)):
#     ax.text(data_new[i, 0], data_new[i, 1], data_new[i, 2], language_codes[i])
#
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
#
# plt.savefig("reduce_dim_3.png")
# plt.show()


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
plt.savefig("reduce_dim_2.png")