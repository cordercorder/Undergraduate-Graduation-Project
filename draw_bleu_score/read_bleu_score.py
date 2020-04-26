import os

source_dir_list = ["final_tests_combine_fr_de_zh_jap_ru_lstm", "final_tests_combine_fr_de_lstm", "final_tests_de_lstm", "final_tests_fr_lstm"]

for source_dir in source_dir_list:
    p = os.path.join("/data/rrjin/Graduation", source_dir)
    data = []
    for item in os.listdir(p):
        if not item.endswith(".txt"):
            continue
        with open(os.path.join(p, item)) as f:
            tmp = f.read().split("\n")
            bleu = None
            for line in tmp:
                idx = line.find("BLEU SCORE:")
                if idx != -1:
                    bleu = float(line[idx+len("BLEU SCORE:"):])
            if bleu is None:
                bleu = 0
        if item.startswith("results"):
            x = int(item[8]) * 10000 + int(item[10:14])
        elif item.startswith("result"):
            x = int(item[7]) * 10000 + int(item[9:13])
        elif item.startswith("repeat"):
            x = int(item[7]) * 10000 * 10000 + int(item[16]) + int(item[18:22])
        data.append((bleu, x))
    data.sort(key=lambda v: v[1])
    print(data)
    res = [str(v[0]) for v in data]
    with open(os.path.join(os.getcwd(), source_dir + ".txt"), "w") as f:
        f.write("\n".join(res))