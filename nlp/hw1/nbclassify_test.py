from nlp.hw1.data_tokenizer import DataTokenizer
import numpy

labels_filename = 'train-labels.txt'
output_filename = 'nboutput.txt'


def nb_test(path):
    absolute_path = path + labels_filename
    label_tokenizer = DataTokenizer(absolute_path)
    labels_dict = label_tokenizer.read_labels()

    absolute_path = path + output_filename
    output_tokenizer = DataTokenizer(absolute_path)
    output_dict = output_tokenizer.read_labels()

    avg_f1 = numpy.mean([get_feature_f1(output_dict, labels_dict, 'positive', 1),
                         get_feature_f1(output_dict, labels_dict, 'negative', 1),
                         get_feature_f1(output_dict, labels_dict, 'truthful', 0),
                         get_feature_f1(output_dict, labels_dict, 'deceptive', 0)])
    print(avg_f1)


def calculate_precision(true_positives, false_positives):
    return true_positives / (true_positives + false_positives)


def calculate_recall(true_positives, false_negatives):
    return true_positives / (true_positives + false_negatives)


def calculate_f1(true_positives, false_positives, false_negatives):
    precision = calculate_precision(true_positives, false_positives)
    recall = calculate_precision(true_positives, false_negatives)
    return 2 * precision * recall / (precision + recall)


def get_feature_f1(output_dict, labels_dict, feature, feature_type):
    false_positives = 0
    true_positives = 0
    false_negatives = 0
    true_negatives = 0

    # Compare results from nboutput.txt
    for key in output_dict:
        predicted_value = output_dict[key]
        actual_value = labels_dict[key]
        if predicted_value[feature_type] == feature and actual_value[feature_type] == feature:
            true_positives += 1
        elif predicted_value[feature_type] == feature and actual_value[feature_type] != feature:
            false_positives += 1
        elif predicted_value[feature_type] != feature and actual_value[feature_type] == feature:
            false_negatives += 1
        elif predicted_value[feature_type] != feature and actual_value[feature_type] != feature:
            true_negatives += 1
    return (calculate_f1(true_positives, false_positives, false_negatives))


nb_test('/Users/anshulip/PycharmProjects/DynamicProg/nlp/hw1/')
