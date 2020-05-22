python -u combine_feature_logistic_classify.py \
    --feature_name syntax_wals \
    --source_dir /data/rrjin/Graduation/data/language_vector \
                /data/rrjin/Graduation/data/hidden_states \
    --prefix combine_all_data_bpe_ \
             hidden_states_ \
    --output_file_name combine_word_vec_hidden_states_logistic_classify_syntax_wals.txt