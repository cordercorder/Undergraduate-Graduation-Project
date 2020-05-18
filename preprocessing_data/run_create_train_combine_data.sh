python -u create_train_combine_data.py \
    --source_directory /data/rrjin/Graduation/data/bible-corpus/parallel_text/en-fr.txt \
                       /data/rrjin/Graduation/data/bible-corpus/parallel_text/de-en.txt \
                       /data/rrjin/Graduation/data/bible-corpus/parallel_text/en-zh.txt \
                       /data/rrjin/Graduation/data/bible-corpus/parallel_text/en-jap.txt \
                       /data/rrjin/Graduation/data/bible-corpus/parallel_text/en-ru.txt \
    --output_directory /data/rrjin/Graduation/data/bible-corpus/train_data \
    --output_file combine_fr_de_zh_jap_ru