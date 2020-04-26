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
    --load bible_model_final_combine_fr_de_zh_jap_ru_lstm \
    --extract_lvs /data/rrjin/Graduation/data/language_vector \
    --word_list fr \
                de \
                zh \
                jap \
                ru \
    --prefix_name combine_fr_de_zh_jap_ru__