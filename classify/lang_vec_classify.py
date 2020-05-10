from __future__ import print_function, division
from sklearn import preprocessing, neighbors, linear_model, multioutput
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
import argparse
import numpy as np
import lang2vec.lang2vec as l2v
import os, sys, csv
import pickle
import pycountry

parser = argparse.ArgumentParser()
parser.add_argument("--random", action='store_true')
parser.add_argument("--majority", action='store_true')
parser.add_argument("--family", action='store_true')
parser.add_argument("--results_path", default="syntax_avg_new.csv", type=str)
parser.add_argument("--bible_langs_path", default="/data/rrjin/Graduation/bible_langs.txt", type=str)
args = parser.parse_args()

with open(args.bible_langs_path) as f:
    lang_codes = f.read().split("\n")

lang_codes.sort()

lang_vec_source_dir = "/data/rrjin/Graduation/data/language_vector"

lang_vec = {}

prefix = "combine_fr_de_zh_jap_ru__"

for item in os.listdir(lang_vec_source_dir):
    if item.startswith(prefix):
        idx = item.find(prefix)
        lang_name = item[idx + len(prefix) : -4][:2]
        lang_name = pycountry.languages.get(alpha_2 = lang_name)
        p = os.path.join(lang_vec_source_dir, item)
        lang_vec[lang_name.alpha_3] = np.load(p)

#Pick feature class
feat_name = "phonology_average"
# typ_feats, typ_feat_names = lang2vec.get(" ".join(lang_codes), feat_name)
typ_feats = l2v.get_features(" ".join(lang_codes), feat_name, header=True)
typ_feat_names = typ_feats["CODE"]

# syntax_avg, syntax_avg_feat_names = lang2vec.get(" ".join(lang_codes), "syntax_average")
syntax_avg = l2v.get_features(" ".join(lang_codes), "syntax_average", header=True)
syntax_avg_feat_names = syntax_avg["CODE"]

# phonology_avg, phonology_avg_feat_names = lang2vec.get(" ".join(lang_codes), "phonology_average")
phonology_avg = l2v.get_features(" ".join(lang_codes), "phonology_average", header=True)
phonology_avg_feat_names = phonology_avg["CODE"]

# inventory_avg, inventory_avg_feat_names = lang2vec.get(" ".join(lang_codes), "inventory_average")
inventory_avg = l2v.get_features(" ".join(lang_codes), "inventory_average", header=True)
inventory_avg_feat_names = inventory_avg["CODE"]

# syntax_knn, syntax_knn_feat_names = lang2vec.get(" ".join(lang_codes), "syntax_knn")
syntax_knn = l2v.get_features(" ".join(lang_codes), "syntax_knn", header=True)
syntax_knn_feat_names = syntax_knn["CODE"]

# phonology_knn, phonology_knn_feat_names = lang2vec.get(" ".join(lang_codes), "phonology_knn")
phonology_knn = l2v.get_features(" ".join(lang_codes), "phonology_knn", header=True)
phonology_knn_feat_names = phonology_knn["CODE"]

# inventory_knn, inventory_knn_feat_names = lang2vec.get(" ".join(lang_codes), "inventory_knn")
inventory_knn = l2v.get_features(" ".join(lang_codes), "inventory_knn", header=True)
inventory_knn_feat_names = inventory_knn["CODE"]

# geog, geog_feat_names = lang2vec.get(" ".join(lang_codes), "geo")
geog = l2v.get_features(" ".join(lang_codes), "geo", header=True)
geog_feat_names = geog["CODE"]

# fam, fam_feat_names = lang2vec.get(" ".join(lang_codes), "fam")
fam = l2v.get_features(" ".join(lang_codes), "fam", header=True)
fam_feat_names = fam["CODE"]

logreg_scores = []
nn_scores = []
random_scores = []
scores = []
scores_ref = []
iterate = len(typ_feats['fra'])
all_preds = []
all_refs = []
all_randoms = []


def generate_features(x):
    if x == "--":
        return -1
    return x


sorted_typ_feats = sorted(typ_feats.items())

train_rate = 0.6

for feat in range(iterate):
    scores_dict = {}
    scores_dict_ref = {}
    preds = []
    refs = []
    f = np.array([generate_features(l[1][feat]) for l in sorted_typ_feats if l[0] != "CODE"])
    #     print(f)
    #     print(type(f[0]))
    lang_indices = np.where(f != -1)  # indices of a language that has feature "feat"
    #     print(lang_indices)
    feat_langs = [lang_codes[l] for l in lang_indices[0]]  # name of a language that has feature "feat"
    #     print(feat_langs)

    if len(feat_langs) == 0:
        print("No language contain a value for feature {}. Skipping".format(typ_feat_names[feat]))
        continue

    X_data = np.zeros((len(feat_langs), 370))
    y_data = np.zeros(len(feat_langs))

    for i, l in enumerate(lang_indices[0]):
        X_data[i] = lang_vec[lang_codes[l]]
        y_data[i] = f[l]

    #     print("before: {}".format(y_data))
    lab_enc = preprocessing.LabelEncoder()
    y_data = lab_enc.fit_transform(y_data)

    if np.all(y_data == y_data[0]):
        print("Feature {} has only one class!".format(typ_feat_names[feat]))
        continue
    #     print("after: {}".format(y_data))

    if len(X_data) < 2:
        print("Data is insufficient")
        continue

    X_train = X_data[:int(len(feat_langs) * train_rate)]
    y_train = y_data[:int(len(feat_langs) * train_rate)]

    if np.all(y_train == y_train[0]):
        print("Train data has only one class!")
        continue

    X_test = X_data[int(len(feat_langs) * train_rate):]
    y_test = y_data[int(len(feat_langs) * train_rate):]

    logistic_model = linear_model.LogisticRegression()
    clf = logistic_model.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print(confidence, len(y_test), sep=", ")