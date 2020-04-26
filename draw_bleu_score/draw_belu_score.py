import matplotlib.pyplot as plt
import os

source_dir = "/data/rrjin/Graduation/draw_bleu_score"
idx = 0
c = ["red", "blue", "purple", None]

for item in os.listdir(source_dir):
    if not item.endswith(".txt"):
        continue
    image_name = item[:-4]
    with open(os.path.join(source_dir, item)) as f:
        data_tmp = f.read().split("\n")
        data = [float(x) * 100 for x in data_tmp]
        # plt.cla()
        # plt.xlabel("valid step")
        # plt.ylabel("bleu")
        # plt.title(image_name)
        if c[idx] is None:
            plt.plot(range(1, len(data)+1), data, label=image_name)
        else:
            plt.plot(range(1, len(data)+1), data, color=c[idx], label=image_name)
        # plt.legend()
        # plt.grid()
        # plt.savefig("./" + image_name + ".png")
        # plt.show()
    idx += 1

plt.xlabel("valid step")
plt.ylabel("bleu")
plt.legend()
plt.grid()
plt.savefig("./all.png")
plt.show()
