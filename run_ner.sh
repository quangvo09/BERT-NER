#!/usr/bin/env bash

  python3 run_ner.py \
    --data_dir=data/  \
    --bert_model=bert-base-uncased  \
    --task_name=ner  \
    --output_dir=out  \
    --max_seq_length=128  \
    --train_batch_size=8  \
    --do_eval  \
    --eval_batch_size=8  \
    --do_lower_case  \
    --num_train_epochs 5 --warmup_proportion=0.4
