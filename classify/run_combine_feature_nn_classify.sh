python -u combine_feature_nn_classify.py \
    --feature_name syntax_wals \
    --source_dir /data/rrjin/Graduation/data/cell_states \
                 /data/rrjin/Graduation/data/language_vector \
    --prefix cell_states_ \
             combine_all_data_bpe_ \
    --gpu_id 1 \
    --output_file_name combine_cell_states_word_vec_nn_classify_syntax_wals.txt