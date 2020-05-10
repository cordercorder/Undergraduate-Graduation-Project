import math
import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--k", type=int)
parser.add_argument("--output_dir")

args, unknown = parser.parse_known_args()


class Position:
    r = 6378.137

    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    @staticmethod
    def rad(d):
        return d * math.pi / 180.0

    @staticmethod
    def get_distance(position1, position2):
        rat_lat1 = Position.rad(position1.latitude)
        rat_lat2 = Position.rad(position2.latitude)

        a = rat_lat1 - rat_lat2
        b = Position.rad(position1.longitude) - Position.rad(position2.longitude)
        s = 2.0 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(rat_lat1) * math.cos(rat_lat2) * math.pow(math.sin(b/2), 2)))
        s = s * Position.r * 1000
        return s


position_data_dir = "/data/rrjin/Graduation/data/wals_features/Languages.csv"
feature_data_dir = "/data/rrjin/Graduation/data/wals_features/Values.csv"

# print(Position.get_distance(Position(6, 36), Position(6, 37)))

df_language = pd.read_csv(position_data_dir)
latitude, longitude = list(df_language["latitude"]), list(df_language["longitude"])
language_id = [str(item) for item in df_language["id"]]
position_list = [Position(lat, lon) for lat, lon in zip(latitude, longitude)]


df_feature = pd.read_csv(feature_data_dir)
feature_lang_id = [str(item) for item in df_feature["id"]]
feature = list(df_feature["domainelement_pk"])

position_data = dict()
for i in range(len(position_list)):
    position_data[language_id[i]] = position_list[i]

feature_data = dict()
for i in range(len(feature_lang_id)):
    feature_data[feature_lang_id[i][4:]] = feature[i]

f = open(os.path.join(args.output_dir, "result" + "_" + str(args.k) + ".txt"), "w")
f.write("id" + "    " + "label" + "    " + "predict" + "\n")

correct = 0

for i, language in enumerate(feature_lang_id):
    pos = position_data[language[4:]]
    tmp = []
    for j, select_language in enumerate(feature_lang_id):
        if i == j:
            continue
        pos_select = position_data[select_language[4:]]
        distance = Position.get_distance(pos, pos_select)
        tmp.append((select_language[4:], distance))
    tmp.sort(key=lambda item: item[1])

    count = dict()
    for item in tmp[:args.k]:
        lan = item[0]
        count[feature_data[lan]] = count.get(feature_data[lan], 0) + 1
    # print(count)
    max_key = -1
    max_value = 0
    for key, value in count.items():
        if value > max_value:
            value = max_value
            max_key = key
    # print(language[4:], max_key)
    f.write(language[4:] + "    " + str(feature_data[language[4:]]) + "    " + str(max_key) + "\n")
    if feature_data[language[4:]] == max_key:
        correct += 1

# print(correct)
f.write("Correct prediction :{}".format(correct) + "\n")
f.write("Accuracy: {}".format(correct / len(feature_lang_id)))
f.close()