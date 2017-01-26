import sys
import json
from nlp.hw1.data_tokenizer import DataTokenizer

labels_filename = 'train-labels.txt'
model_filename = 'nbmodel.txt'
output_filename = 'nboutput.txt'
test_filename = 'test-text.txt'


def read_model(path):
    model = None
    absolute_path_model = path + model_filename
    with open(absolute_path_model, 'r') as f:
        model = json.load(f)
    f.close()
    return model


def classify(path):
    output_file = open(path + output_filename, 'w')
    output_format = '{} {} {}\n'
    absolute_path = path + test_filename
    tokenizer = DataTokenizer(absolute_path)
    model = read_model(path)

    while tokenizer.has_line():
        line = tokenizer.next_line()
        data_id = tokenizer.next_id()

        # Compute class prediction and output
        truthful_pos_class = predict_feature(line, model['+t'])
        truthful_neg_class = predict_feature(line, model['-t'])
        deceptive_pos_class = predict_feature(line, model['+d'])
        deceptive_neg_class = predict_feature(line, model['-d'])

        genuine_class = None
        sentiment_class = None
        if max(truthful_neg_class, truthful_pos_class) > max(deceptive_neg_class, deceptive_pos_class):
            genuine_class = 'truthful'
        else:
            genuine_class = 'deceptive'
        if max(truthful_neg_class, deceptive_neg_class) > max(deceptive_pos_class, truthful_pos_class):
            sentiment_class = 'negative'
        else:
            sentiment_class = 'positive'

        output_file.write(output_format.format(data_id, genuine_class, sentiment_class))

    tokenizer.close()
    output_file.close()


def predict_feature(line, model_feature):
    # prior probability logs
    feature1_probability = model_feature[1]
    for word in line:
        if word in model_feature[0]:
            feature1_probability += model_feature[0][word]
    return feature1_probability


classify('/Users/anshulip/PycharmProjects/DynamicProg/nlp/hw1_copy/')
