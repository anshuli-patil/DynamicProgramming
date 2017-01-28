import sys
import json
from nlp.hw1.data_tokenizer import DataTokenizer


labels_filename = 'train-labels.txt'
model_filename = 'nbmodel.txt'
output_filename = 'nboutput.txt'
test_filename = 'test-text.txt'


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
        truthful_pos_class = predict_feature(line, model['+t'])
        truthful_neg_class = predict_feature(line, model['-t'])
        deceptive_pos_class = predict_feature(line, model['+d'])
        deceptive_neg_class = predict_feature(line, model['-d'])

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


classify(str(sys.argv[1]))
