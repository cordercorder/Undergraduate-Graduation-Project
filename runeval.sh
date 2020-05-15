# nohup bash runeval.sh >runeval_log.txt 2>&1 &
python -u trainer.py \
    --dynet-devices CPU,GPU:2 \
    --eval \
    --model_type=attention \
    --reader_mode parallel \
    --train_src /data/rrjin/Graduation/data/bible-corpus/eval_data/eval_jap_zh_src1.txt \
    --train_tgt /data/rrjin/Graduation/data/bible-corpus/eval_data/eval_jap_zh_tgt1.txt \
    --test_src /data/rrjin/Graduation/data/bible-corpus/eval_data/eval_jap_zh_src1.txt \
    --test_tgt /data/rrjin/Graduation/data/bible-corpus/eval_data/eval_jap_zh_tgt1.txt \
    --trainer=adam \
    --directory_name eval_jap_zh \
    --results_filename result1 \
    --load bible_model_final_combine_all_data_bpe