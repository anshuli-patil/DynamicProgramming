import sys
import json
import math
from nlp.hw1.data_tokenizer import DataTokenizer

model_filename = 'nbmodel.txt'
output_filename = 'nboutput.txt'


def read_model():
    model = None
    absolute_path_model = model_filename
    with open(absolute_path_model, 'r') as f:
        model = json.load(f)
    f.close()
    return model


def classify(test_filepath):
    output_file = open(output_filename, 'w')
    output_format = '{} {} {}\n'
    absolute_path = test_filepath
    tokenizer = DataTokenizer(absolute_path)
    model = read_model()

    while tokenizer.has_line():
        line = tokenizer.next_line()
        data_id = tokenizer.next_id()

        # Compute class prediction and output
        genuine_class = predict_feature(line, model['t'], model['d'], 'truthful', 'deceptive')
        sentiment_class = predict_feature(line, model['+'], model['-'], 'positive', 'negative')

        output_file.write(output_format.format(data_id, genuine_class, sentiment_class))

    tokenizer.close()
    output_file.close()


def predict_feature(line, model_feature1, model_feature2, feature1_name, feature2_name):
    # prior probability logs
    feature1_probability = model_feature1[1]
    feature2_probability = model_feature2[1]
    for word in line:
        if word in model_feature1[0]:
            feature1_probability += model_feature1[0][word]
        if word in model_feature2[0]:
            feature2_probability += model_feature2[0][word]
    if feature1_probability > feature2_probability:
        return feature1_name
    else:
        return feature2_name

'''
python nbclassify.py /path/to/text/file
'''
classify(str(sys.argv[1]))
