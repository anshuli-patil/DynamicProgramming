import sys
import json
import math
from collections import defaultdict
from nlp.hw1.data_tokenizer import DataTokenizer

model_filename = 'nbmodel.txt'


def get_feature(labels_dict, data_id):
    return labels_dict[data_id]


def read_sample_data(textfile_path, labelfile_path):
    absolute_path = labelfile_path
    label_tokenizer = DataTokenizer(absolute_path)
    labels_dict = label_tokenizer.read_labels()

    absolute_path = textfile_path
    tokenizer = DataTokenizer(absolute_path)

    occurrences_pos_truth = defaultdict(int)
    occurrences_pos_deceptive = defaultdict(int)
    occurrences_neg_truth = defaultdict(int)
    occurrences_neg_deceptive = defaultdict(int)

    pos_truth_count = 0
    neg_truth_count = 0
    pos_deceptive_count = 0
    neg_deceptive_count = 0

    vocabulary = set()
    while tokenizer.has_line():
        line = tokenizer.next_line()
        data_id = tokenizer.next_id()
        tagged_feature = get_feature(labels_dict, data_id)

        pos_truth, neg_truth, pos_deceptive, neg_deceptive = count_feature_occurrences(vocabulary, line, tagged_feature,
                                                                                       occurrences_pos_truth,
                                                                                       occurrences_pos_deceptive,
                                                                                       occurrences_neg_truth,
                                                                                       occurrences_neg_deceptive)
        pos_truth_count += pos_truth
        neg_truth_count += neg_truth
        pos_deceptive_count += pos_deceptive
        neg_deceptive_count += neg_deceptive

    tokenizer.close()
    total_count = pos_truth_count + neg_truth_count + pos_deceptive_count + neg_deceptive_count
    prior_prob_pos_truth = pos_truth_count / total_count
    prior_prob_neg_truth = neg_truth_count / total_count
    prior_prob_pos_deceptive = pos_deceptive_count / total_count
    prior_prob_neg_deceptive = neg_deceptive_count / total_count

    return vocabulary, [(occurrences_pos_truth, prior_prob_pos_truth),
                        (occurrences_pos_deceptive, prior_prob_pos_deceptive),
                        (occurrences_neg_truth, prior_prob_neg_truth),
                        (occurrences_neg_deceptive, prior_prob_neg_deceptive)]


def count_feature_occurrences(vocabulary, line, tagged_feature, occurrences_pos_truth, occurrences_pos_deceptive,
                              occurrences_neg_truth,
                              occurrences_neg_deceptive):
    pos_truth_count = 0
    neg_truth_count = 0
    pos_deceptive_count = 0
    neg_deceptive_count = 0

    if tagged_feature == ('deceptive', 'positive'):
        pos_deceptive_count = 1
        increase_count(occurrences_pos_deceptive, line, vocabulary)
    elif tagged_feature == ('deceptive', 'negative'):
        neg_deceptive_count = 1
        increase_count(occurrences_neg_deceptive, line, vocabulary)
    elif tagged_feature == ('truthful', 'positive'):
        pos_truth_count = 1
        increase_count(occurrences_pos_truth, line, vocabulary)
    elif tagged_feature == ('truthful', 'negative'):
        neg_truth_count = 1
        increase_count(occurrences_neg_truth, line, vocabulary)
    delete_numbers(occurrences_pos_deceptive)
    delete_numbers(occurrences_neg_deceptive)
    delete_numbers(occurrences_pos_truth)
    delete_numbers(occurrences_neg_truth)
    return pos_truth_count, neg_truth_count, pos_deceptive_count, neg_deceptive_count


def estimate_probability(textfile_path, labelfile_path):
    vocabulary, data_results = read_sample_data(textfile_path, labelfile_path)
    for i in range(4):
        fill_missing(data_results[i][0], vocabulary)
        smooth_normalize(data_results[i][0])

    return {'+t': (data_results[0][0], math.log(data_results[0][1])),
            '+d': (data_results[1][0], math.log(data_results[1][1])),
            '-t': (data_results[2][0], math.log(data_results[2][1])),
            '-d': (data_results[3][0], math.log(data_results[3][1]))}


def fill_missing(occurrences_dict_complement, occurrences_dict):
    for word in occurrences_dict:
        if word not in occurrences_dict_complement:
            occurrences_dict_complement[word] = 0


def smooth_normalize(occurrences_dict):
    if '' in occurrences_dict:
        del occurrences_dict['']
    total_count = 0

    for key in occurrences_dict:
        # occurrences_dict[key] += 1
        total_count += occurrences_dict[key]

    # taking log to prevent underflow
    for key in occurrences_dict:
        if occurrences_dict[key] == 0:
            occurrences_dict[key] = 1
        else:
            occurrences_dict[key] = math.log(occurrences_dict[key] / total_count)
    return


def delete_numbers(dict_feature):
    delete_keys = []
    for key in dict_feature:
        if key.isdigit():
            delete_keys.append(key)
    for digits in delete_keys:
        del dict_feature[digits]


def increase_count(dict_feature, line, vocabulary):
    """
    :type dict_feature: dict
    """
    for word in line:
        if word.isdigit() and word in dict_feature:
            del dict_feature[word]
            continue
        vocabulary.add(word)
        dict_feature[word] += 1
    return


def print_dict(dictionary):
    for key in dictionary:
        print(key, dictionary[key])


def create_model(textfile_path, labelfile_path):
    model = estimate_probability(textfile_path, labelfile_path)
    absolute_path_model = model_filename
    with open(absolute_path_model, 'w') as f:
        json.dump(model, f)
    f.close()


create_model(str(sys.argv[1]), str(sys.argv[2]))
