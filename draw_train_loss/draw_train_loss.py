import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--train_log_file", required=True)
parser.add_argument("--output_file_name", required=True)
parser.add_argument("--color")
parser.add_argument("--title")

args, unknown = parser.parse_known_args()

loss = []

with open(args.train_log_file) as f:
    data = f.read().split("\n")
    for line in data:
        if "lr" in line and "Loss" in line:
            l = line.find("Loss: ") + len("Loss: ")
            r = line[l:].find(" ") + l
            loss.append(float(line[l:r]))

x = list(range(len(loss)))
plt.xlabel("log_train_step")
plt.ylabel("loss")
if args.color:
    plt.plot(x, loss, label=args.title, color=args.color)
else:
    plt.plot(x, loss, label=args.title)
plt.title(args.title)
plt.legend()
plt.grid()
plt.savefig("./" + args.output_file_name)
plt.show()