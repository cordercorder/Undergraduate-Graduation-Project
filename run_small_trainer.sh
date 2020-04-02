export LD_LIBRARY_PATH=/home/rrjin/anaconda3/envs/ml2/lib/:$LD_LIBRARY_PATH

python -u trainer.py \
    --dynet-mem 2000 \
    --model_type=attention \
    --input_dim=256 \
    --hidden_dim=256 \
    --minibatch_size=20 \
    --reader_mode=parallel \
    --percent_valid=100 \
    --train_src=/data/rrjin/Graduation/data/bible-corpus/train_data/part_of_train_src_zh.txt \
    --train_tgt=/data/rrjin/Graduation/data/bible-corpus/train_data/part_of_train_tgt_en.txt \
    --trainer=adam \
    --log_valid_every_n=200 \
    --save=test_bible_model_final \
    --log_output=test_bible_model_final_appended.log
