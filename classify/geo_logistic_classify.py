import pycountry
import os
import numpy as np
import argparse
import lang2vec.lang2vec as l2v
from sklearn import preprocessing, neighbors, linear_model, multioutput

source_dir = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"

parser = argparse.ArgumentParser()
parser.add_argument("--feature_name", required=True)
parser.add_argument("--output_file_name", required=True)

args, unknown = parser.parse_known_args()


def get_language_alpha3(language_code):
    if len(language_code) == 2:
        ans = pycountry.languages.get(alpha_2 = language_code)
    elif len(language_code) == 3:
        ans = pycountry.languages.get(alpha_3 = language_code)
    else:
        return "-1"
    if ans is not None:
        return ans.alpha_3
    else:
        return "unknown language"


def check_alpha3(alpha3):
    if alpha3 != "unknown language" and alpha3 in l2v.LANGUAGES:
        return True
    return False


langcode_to_alpha3 = {"jap": "jpn"}

for lang in os.listdir(source_dir):
    # Get ISO 639-3 codes according to abbreviations of languages
    s = lang[:-4]
    language1, language2 = s.split("-")
    language1_alpha3, language2_alpha3 = get_language_alpha3(language1), get_language_alpha3(language2)
    if check_alpha3(language1_alpha3):
        langcode_to_alpha3[language1] = language1_alpha3
    if check_alpha3(language2_alpha3):
        langcode_to_alpha3[language2] = language2_alpha3

langcode_to_alpha3.pop("en")

lang_alpha3 = list(langcode_to_alpha3.values())
feature_name = args.feature_name
features = l2v.get_features(lang_alpha3, feature_name, header=True)

features_geo = l2v.get_features(lang_alpha3, "geo", header=True)

lang_alpha3.sort()  # fix order

X = [features_geo[lang] for lang in lang_alpha3]
train_data_rate = 0.7

X_train = X[:int(len(X)*train_data_rate)]
X_test = X[int(len(X)*train_data_rate):]

score_dict = {}

f = open(os.path.join(os.getcwd(), args.output_file_name), "w")

for feat in range(len(features["CODE"])):
    Y = [features[lang][feat] if features[lang][feat] != "--" else -1 for lang in lang_alpha3]
    lab_enc = preprocessing.LabelEncoder()
    Y = lab_enc.fit_transform(Y)

    Y_train = Y[:int(len(X) * train_data_rate)]
    Y_test = Y[int(len(X) * train_data_rate):]

    if np.all(np.array(Y_train) == Y_train[0]):
        print("Feature {} has only one class!".format(features["CODE"][feat]))
        f.write("Feature {} has only one class!\n".format(features["CODE"][feat]))
        continue

    logistic_model = linear_model.LogisticRegression(max_iter=3000)
    clf = logistic_model.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    score_dict[features["CODE"][feat]] = score

    print("Feature {} accuracy is {}".format(features["CODE"][feat], score))
    f.write("Feature {} accuracy is {}\n".format(features["CODE"][feat], score))

f.close()