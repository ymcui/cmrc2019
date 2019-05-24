#!/bin/bash
set -ex

python run_cmrc2019_baseline.py \
	--bert_model bert-base-chinese \
	--vocab_file ./bert_weights_chinese/vocab.txt \
	--bert_config_file ./bert_weights_chinese/bert_config.json \
	--init_checkpoint ./bert_weights_chinese/pytorch_model.bin \
	--do_train \
	--do_predict \
	--train_file cmrc2019_train.json \
	--predict_file cmrc2019_trial.json \
	--train_batch_size 24 \
	--learning_rate 2e-5 \
	--num_train_epochs 3.0 \
	--max_seq_length 512 \
	--output_dir ./output_model