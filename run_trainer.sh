# nohup sh run_trainer.sh >./train_logs/combine_fr_de_zh_jap_ru_log_lstm.txt 2>&1 &
python -u trainer.py \
    --dynet-gpu \
    --input_dim 370 \
    --hidden_dim 370 \
    --model_type attention \
    --minibatch_size 32 \
    --percent_valid 800 \
    --reader_mode parallel \
    --train_src /data/rrjin/Graduation/data/bible-corpus/train_data/combine_fr_de_zh_jap_ru_src.txt \
    --train_tgt /data/rrjin/Graduation/data/bible-corpus/train_data/combine_fr_de_zh_jap_ru_tgt.txt \
    --trainer adam \
    --save bible_model_final_combine_fr_de_zh_jap_ru_lstm \
    --log_output bible_model_final_appended_combine_fr_de_zh_jap_ru_lstm.log \
    --results_filename result \
    --directory_name final_tests_combine_fr_de_zh_jap_ru_lstm