from nlp.hw1.data_tokenizer import DataTokenizer


labels_filename = 'train-labels.txt'
output_filename = 'nboutput.txt'


def nb_test( path):
    absolute_path = path + labels_filename
    label_tokenizer = DataTokenizer(absolute_path)
    labels_dict = label_tokenizer.read_labels()

    absolute_path = path + output_filename
    output_tokenizer = DataTokenizer(absolute_path)
    output_dict = output_tokenizer.read_labels()

    false_positives = 0
    true_positives = 0
    false_negatives = 0
    true_negatives = 0

    correct = 0
    wrong = 0
    # Compare results from nboutput.txt
    for key in output_dict:
        value = output_dict[key]
        actual_value = labels_dict[key]
        if value == actual_value:
            correct += 1
        else:
            wrong += 1
    print(correct, wrong)


def calculate_precision(true_positives, false_positives):
    return true_positives / (true_positives + false_positives)


def calculate_recall(true_positives, false_negatives):
    return true_positives / (true_positives + false_negatives)


def calculate_f1(true_positives, false_positives, false_negatives):
    precision = calculate_precision(true_positives, false_positives)
    recall = calculate_precision(true_positives, false_negatives)
    return 2 * precision * recall / (precision + recall)

nb_test('/Users/anshulip/PycharmProjects/DynamicProg/nlp/hw1/')
