#!/bin/sh
num_operations=32000

merge_file_src=/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_src.txt
merge_file_tgt=/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_tgt.txt

merge_codes_file_src=/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_src_bpe_codes.txt
merge_out_file_src=/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_src_bpe.txt

merge_codes_file_tgt=/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_tgt_bpe_codes.txt
merge_out_file_tgt=/data/rrjin/Graduation/data/bible-corpus/train_data/merge_combine_all_data_tgt_bpe.txt

subword-nmt learn-bpe -s ${num_operations} < ${merge_file_src} > ${merge_codes_file_src}
subword-nmt apply-bpe -c ${merge_codes_file_src} < ${merge_file_src} > ${merge_out_file_src}

subword-nmt learn-bpe -s ${num_operations} < ${merge_file_tgt} > ${merge_codes_file_tgt}
subword-nmt apply-bpe -c ${merge_codes_file_tgt} < ${merge_file_tgt} > ${merge_out_file_tgt}