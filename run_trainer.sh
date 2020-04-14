# nohup sh run_trainer.sh >./train_logs/combined_fr_de_log.txt 2>&1 &
python -u trainer.py \
    --dynet-mem 3500 \
    --dynet-gpu \
    --input_dim 350 \
    --hidden_dim 350 \
    --model_type=attention \
    --minibatch_size=32 \
    --percent_valid=1000 \
    --reader_mode=parallel \
    --train_src=/data/rrjin/Graduation/data/bible-corpus/train_data/combine_fr_de_src.txt \
    --train_tgt=/data/rrjin/Graduation/data/bible-corpus/train_data/combine_fr_de_tgt.txt \
    --trainer=adam \
    --save=bible_model_final_combined_fr_de \
    --log_output=bible_model_final_appended_combined_fr_de.log