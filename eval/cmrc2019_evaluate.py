# -*- coding: utf-8 -*-
'''
Evaluation script for CMRC 2019
'''
from __future__ import print_function
import string
import re
import argparse
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#
def compare_list(ground_truth, prediction):
	right_count = 0
	min_len = len(ground_truth) if len(ground_truth)<len(prediction) else len(prediction)
	gap_count = len(ground_truth) - min_len

	for k in range(min_len):
		if str(ground_truth[k]) == str(prediction[k]):
			right_count += 1

	final_right_count = right_count - gap_count
	if final_right_count < 0:
		final_right_count = 0 
	return final_right_count

#
def evaluate(ground_truth_file, prediction_file):
	qac = 0
	pac = 0
	qac_score = 0
	pac_score = 0
	total_question_count = 0
	skip_question_count = 0
	total_passage_count = 0

	for instance in ground_truth_file["data"]:
		context 	= instance["context"]
		context_id 	= instance["context_id"]
		choices 	= instance["choices"]
		answers 	= instance["answers"]

		predictions = []
		if context_id not in prediction_file:
			sys.stderr.write("Not found context_id in prediction: {}\n".format(context_id))
			right_question_count = 0
		else:
			predictions	= prediction_file[context_id]
			right_question_count = compare_list(answers, predictions)

		qac += right_question_count
		pac += (right_question_count == len(answers))

		total_question_count += len(answers)
		skip_question_count += len(answers) - len(predictions)
		total_passage_count += 1

	qac_score = 100.0 * qac / total_question_count
	pac_score = 100.0 * pac / total_passage_count

	if skip_question_count:
		sys.stderr.write("***Number of predicted samples is not equal to ground truth!***")

	return qac_score, pac_score, total_question_count, skip_question_count


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Evaluation Script for CMRC 2019')
	parser.add_argument('dataset_file', help='Official dataset file')
	parser.add_argument('prediction_file', help='Your prediction File')
	args = parser.parse_args()
	ground_truth_file   = json.load(open(args.dataset_file, 'rb'))
	prediction_file     = json.load(open(args.prediction_file, 'rb'))
	QAC, PAC, TOTAL, SKIP = evaluate(ground_truth_file, prediction_file)

	print('FILE: {}'.format(args.prediction_file))
	print('QAC: {}'.format(QAC))
	print('PAC: {}'.format(PAC))
	print('TOTAL: {}'.format(TOTAL))
	print('SKIP: {}'.format(SKIP))

