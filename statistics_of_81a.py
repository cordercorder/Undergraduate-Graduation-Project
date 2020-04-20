import os
import matplotlib.pyplot as plt
import collections

source_dir = "/data/rrjin/Graduation/data/wals_features"

data_all = collections.defaultdict(list)

feature_id={"383":"SOV", "384":"SVO", "385":"VSO", "386":"VOS", "387":"OVS", "388":"OSV", "389":"None"}

for item in os.listdir(source_dir):
    if item.startswith("result"):
        count = dict()
        count_correct = dict()
        with open(os.path.join(source_dir, item)) as f:
            data = f.read().split("\n")
            data = data[1:1378]
            for line in data:
                tmp = line.split()
                count[tmp[1]] = count.get(tmp[1], 0) + 1
                if tmp[1] == tmp[2]:
                    count_correct[tmp[1]] = count_correct.get(tmp[1], 0) + 1
        print(item)
        print(count)
        print(count_correct)
        for key, value in count.items():
            tmp = count_correct.get(key, 0)
            data_all[key].append((tmp/value, int(item[7])))
            print("{} rate: {}".format(key, tmp/value))
        print("\n")


plt.xlabel("k")
plt.ylabel("rate")

for key in data_all.keys():
    data_all[key].sort(key=lambda x: x[1])
    tmp = []
    for item in data_all[key]:
        tmp.append(item[0])
    plt.plot(range(1, 9), tmp, label=feature_id[key])
plt.legend()
plt.savefig("./baseline_data_all.png")
plt.show()