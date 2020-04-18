# nohup sh run_trainer.sh >./train_logs/repeat_3_de_log_lstm.txt 2>&1 &
python -u trainer.py \
    --dynet-mem 3500 \
    --dynet-gpu \
    --input_dim 350 \
    --hidden_dim 350 \
    --model_type attention \
    --minibatch_size 32 \
    --percent_valid 500 \
    --reader_mode parallel \
    --train_src /data/rrjin/Graduation/data/bible-corpus/train_data/de_src.txt \
    --train_tgt /data/rrjin/Graduation/data/bible-corpus/train_data/de_tgt.txt \
    --trainer adam \
    --save bible_model_final_de_lstm \
    --load bible_model_final_de_lstm \
    --log_output bible_model_final_appended_de_lstm.log \
    --results_filename repeat_3_result \
    --directory_name final_tests_de_lstm