# nohup sh run_trainer.sh >./train_logs/combined_all_data_bpe_log_lstm.txt 2>&1 &
python -u trainer.py \
    --dynet-gpu \
    --input_dim 512 \
    --hidden_dim 512 \
    --model_type attention \
    --minibatch_size 32 \
    --reader_mode parallel \
    --train_src /data/rrjin/Graduation/data/bible-corpus/train_data/train_combine_all_data_src_bpe.txt \
    --train_tgt /data/rrjin/Graduation/data/bible-corpus/train_data/train_combine_all_data_tgt_bpe.txt \
    --valid_src /data/rrjin/Graduation/data/bible-corpus/train_data/test_combine_all_data_src_bpe.txt \
    --valid_tgt /data/rrjin/Graduation/data/bible-corpus/train_data/test_combine_all_data_tgt_bpe.txt \
    --log_train_every_n 50000 \
    --trainer adam \
    --save bible_model_final_combine_all_data_bpe \
    --log_output bible_model_final_appended_combine_all_data_bpe.log \
    --results_filename result \
    --directory_name final_tests_combine_all_data_bpe