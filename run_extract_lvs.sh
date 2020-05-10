python -u trainer.py \
    --dynet-gpu \
    --input_dim 512 \
    --hidden_dim 512 \
    --model_type attention \
    --minibatch_size 32 \
    --reader_mode parallel \
    --train_src /data/rrjin/Graduation/data/bible-corpus/train_data/train_combine_all_data_src_bpe.txt \
    --train_tgt /data/rrjin/Graduation/data/bible-corpus/train_data/train_combine_all_data_tgt_bpe.txt \
    --trainer adam \
    --load bible_model_final_combine_all_data_bpe \
    --extract_lvs /data/rrjin/Graduation/data/language_vector \
    --word_list sl \
                ar \
                agr \
                bsn \
                kn \
                acu \
                de \
                sv \
                dik \
                ch \
                cjp \
                wo \
                gd \
                cak \
                hy \
                mi \
                he \
                sn \
                nhg \
                pot \
                quc \
                shi \
                tr \
                rom \
                ml \
                te \
                crp \
                ko \
                no \
                tmh \
                cs \
                sr \
                ceb \
                cop \
                pl \
                hr \
                zh \
                fr \
                vi \
                tl \
                ne \
                af \
                syr \
                ojb \
                id \
                chq \
                gu \
                is \
                gv \
                mam \
                wal \
                quw \
                xh \
                el \
                so \
                pes \
                sk \
                jak \
                fi \
                it \
                ss \
                lv \
                ee \
                hu \
                bg \
                eo \
                dje \
                da \
                jiv \
                th \
                plt \
                am \
                es \
                et \
                la \
                eu \
                ro \
                djk \
                nl \
                hi \
                ppk \
                usp \
                my \
                dop \
                pck \
                kek \
                pt \
                lt \
                uk \
                mr \
                amu \
                kbh \
                chr \
                cni \
                zu \
                ru \
                gbi \
                sq \
                ake \
                jap \
                kab \
    --prefix_name combine_all_data_bpe_