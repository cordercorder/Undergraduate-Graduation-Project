export LD_LIBRARY_PATH=/home/rrjin/anaconda3/envs/ml2/lib/:$LD_LIBRARY_PATH

python -u trainer.py \
    --dynet-mem 10000 \
    --model_type=attention \
    --input_dim=256 \
    --hidden_dim=256 \
    --minibatch_size=32 \
    --reader_mode=parallel \
    --percent_valid=6 \
    --train_src=/data/rrjin/Graduation/data/bible-corpus/train_data/train_src_zh.txt \
    --train_tgt=/data/rrjin/Graduation/data/bible-corpus/train_data/train_tgt_en.txt \
    --trainer=adam \
    --save=bible_model_final \
    --log_output=bible_model_final_appended.log
