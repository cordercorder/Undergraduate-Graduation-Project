import pycountry
import os
import numpy as np
import argparse
import lang2vec.lang2vec as l2v
from sklearn import preprocessing, neighbors, linear_model, multioutput


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


parser = argparse.ArgumentParser()
parser.add_argument("--feature_name", required=True)
parser.add_argument("--output_file_name", required=True)
parser.add_argument("--source_dir", nargs="+")  # position of language vectors
parser.add_argument("--prefix", nargs="+")

args, unknown = parser.parse_known_args()

language_codes_dir = "/data/rrjin/Graduation/data/bible-corpus/parallel_text"


source_dir = args.source_dir
prefix = args.prefix

assert len(prefix) == len(source_dir)

langcode_to_alpha3 = {"jap": "jpn"}


def get_combine_features(langcode):
    ans = []
    for i in range(len(prefix)):
        p = os.path.join(source_dir[i], prefix[i] + langcode + ".npy")
        assert os.path.exists(p)
        ans.append(np.load(p))
    return np.concatenate(ans)


features_langvec = {"jpn": get_combine_features("jap")}


for lang in os.listdir(language_codes_dir):
    # Get ISO 639-3 codes according to abbreviations of languages
    s = lang[:-4]
    language1, language2 = s.split("-")
    language1_alpha3, language2_alpha3 = get_language_alpha3(language1), get_language_alpha3(language2)

    if check_alpha3(language1_alpha3):
        langcode_to_alpha3[language1] = language1_alpha3

        if language1 != "en":

            tmp = get_combine_features(language1)
            features_langvec[language1_alpha3] = tmp

    if check_alpha3(language2_alpha3):
        langcode_to_alpha3[language2] = language2_alpha3

        if language2 != "en":

            tmp = get_combine_features(language2)
            features_langvec[language2_alpha3] = tmp

langcode_to_alpha3.pop("en")


lang_alpha3 = list(langcode_to_alpha3.values())

feature_name = args.feature_name
features = l2v.get_features(lang_alpha3, feature_name, header=True)

lang_alpha3.sort()  # fix order


X = [features_langvec[lang] for lang in lang_alpha3]
train_data_rate = 0.7

score_dict = {}

f = open(os.path.join(os.getcwd(), args.output_file_name), "w")

for feat in range(len(features["CODE"])):
    Y = [features[lang][feat] if features[lang][feat] != "--" else -1 for lang in lang_alpha3]

    idx = [i for i in range(len(Y)) if Y[i] != -1]

    train_set = np.array([(X[i], Y[i]) for i in idx])

    if len(train_set) == 0:
        print("Feature {} is not available in all 101 languages!".format(features["CODE"][feat]))
        f.write("Feature {} is not available in all 101 languages!\n".format(features["CODE"][feat]))
        continue

    lab_enc = preprocessing.LabelEncoder()
    train_set[:, 1] = lab_enc.fit_transform(train_set[:, 1])

    X_train = train_set[:int(len(train_set) * train_data_rate), 0]
    Y_train = train_set[:int(len(train_set) * train_data_rate), 1]

    X_test = train_set[int(len(train_set) * train_data_rate):, 0]
    Y_test = train_set[int(len(train_set) * train_data_rate):, 1]

    if len(X_train) == 0:
        print("Feature {} has no train data!".format(features["CODE"][feat]))
        f.write("Feature {} has no train data!\n".format(features["CODE"][feat]))
        continue

    if len(X_test) == 0:
        print("Feature {} has no test data!".format(features["CODE"][feat]))
        f.write("Feature {} has no test data!\n".format(features["CODE"][feat]))
        continue

    if np.all(Y_train == Y_train[0]):
        print("Feature {} has only one class!".format(features["CODE"][feat]))
        f.write("Feature {} has only one class!\n".format(features["CODE"][feat]))
        continue

    logistic_model = linear_model.LogisticRegression(max_iter=3000)
    clf = logistic_model.fit(X_train.tolist(), Y_train.tolist())
    score = clf.score(X_test.tolist(), Y_test.tolist())
    score_dict[features["CODE"][feat]] = score
    print("Feature {} accuracy is {}, train dataset has {} element, test dataset has {} element".format(features["CODE"][feat], score, len(X_train), len(X_test)))
    f.write("Feature {} accuracy is {}, train dataset has {} element, test dataset has {} element\n".format(features["CODE"][feat], score, len(X_train), len(X_test)))

f.close()
