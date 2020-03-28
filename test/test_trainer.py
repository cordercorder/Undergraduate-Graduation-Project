import sys
sys.path.append("/data/rrjin/Graduation")
# reload(sys)
# sys.setdefaultencoding("utf-8")
import util
source = "/data/rrjin/Graduation/data/bible-corpus/train_data/"
src_name = "train_src_zh.txt.vocab-parallel-src"
train_src = "/data/rrjin/Graduation/data/bible-corpus/train_data/train_src_zh.txt"

src_reader = util.get_reader("parallel")(train_src, mode="parallel", begin="<s>", end="<e>")

src_vocab = util.Vocab.load_from_corpus(src_reader, remake=False, src_or_tgt="src")
print(src_vocab.unk, src_vocab.START_TOK, src_vocab.END_TOK)

cnt = 0
print(sys.getdefaultencoding())