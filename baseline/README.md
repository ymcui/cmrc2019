## Baseline System for CMRC 2019

We provide a simple BERT-based baseline system (PyTorch version) for participants. </br>

### Updates
May 28, 2019 Baseline system and trial results have been updated. All participants are encouraged to take a look.

May 27, 2019 We've discovered an issue in the baseline code and will be updated shortly. Thank **@fanyangfanyang** for reporting the issue.



### Note

- We assume that you have been familiar with [PyTorch BERT](https://github.com/huggingface/pytorch-pretrained-BERT). </br>

- We are NOT responsible for helping participants in building up their baseline systems.

- The baseline codes are only for helping participants to better understand the basic routine of this task.


## Content

| Section | Description |
|-|-|
| [Requirements](#Requirements) | Describe dependency requirements |
| [Preparations](#Preparation) | Describe preparation steps before running |
| [Training](#Training) | Training command line  |
| [Testing](#Testing) | Testing command line |
| [Baseline Results](#Baseline-Results) | Baseline Results |
| [Acknowledgement](#Acknowledgement) | - |


## Requirements
Our codes are adapted from [PyTorch BERT](https://github.com/huggingface/pytorch-pretrained-BERT). </br>
If you are familiar with that, there will be nothing special here. </br>
Specifically, we use `pytorch 1.0.0` for baseline system.

## Preparation

### Step 1: Clone the repository

```
git clone https://github.com/ymcui/cmrc2019.git
```

### Step 2: Prepare Chinese BERT weights (PyTorch version)
You have to get pre-trained Chinese BERT for initialization purpose. </br>
Please infer official guidelines through: https://github.com/huggingface/pytorch-pretrained-BERT#Command-line-interface


## Training
We assume that all the files are placed in the correct path. </br>
Pre-trained Chinese BERT weights (PyTorch version) should be placed in `bert_weights_chinese` folder.

```
python run_cmrc2019_baseline.py \
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
```

We use one NVIDIA V100 (32GB) for training and roughly take 4~5 hours.


## Testing
If you have successfully trained your model, you could use the following command for testing your model on the testing sets.
```
python run_cmrc2019_baseline.py \
	--bert_model bert-base-chinese \
	--vocab_file ./bert_weights_chinese/vocab.txt \
	--bert_config_file ./bert_weights_chinese/bert_config.json \
	--do_predict \
	--predict_file cmrc2019_trial.json \
	--max_seq_length 512 \
	--output_dir ./output_model
```

After running testing script, there will be a `predictions.json` file generated under `--output_dir` folder.

Then we can use official evaluation script `cmrc2019_evaluate.py` (in this GitHub `eval` directory) to get final results.

```
python cmrc2019_evaluate.py cmrc2019_trial.json predictions.json
```

And the results will be shown like

```
FILE: predictions.json
QAC: 71.9414893617
PAC: 28.7769784173
TOTAL: 1504
SKIP: 0
```


## Baseline Results
We provide a BERT-based baseline system for participants (will be available shortly).
Results on other sets will be annouced later.

Note: Due to the non-determinism on GPU, your results will be slightly different.

| Data | QAC | PAC | 
| :------ | :-----: | :-----: | 
| Trial data | 71.941% | 28.776% |
| Development data | - | - |
| Qualifying data | - | - |
| Test data | - | - |


## Acknowledgement
Our codes are adapted from [PyTorch BERT](https://github.com/huggingface/pytorch-pretrained-BERT).

