import string


class DataTokenizer:

    id_length = 20
    file_path = ''
    datafile = None
    next_line_text = None
    next_id_text = None

    def __init__(self, path):
        self.file_path = path
        self.datafile = open(path)

    def has_line(self):
        self.next_line_text = self.datafile.readline()
        return self.next_line_text is not None and self.next_line_text != ''

    def next_line(self):
        if self.next_line_text is None:
            self.next_line_text = self.datafile.readline()
        return_data = self.next_line_text[self.id_length + 1:]
        self.next_id_text = self.next_line_text[:self.id_length]
        self.next_line_text = None
        return self.filter_tokens(return_data)

    def next_id(self):
        """
        gets the data ID from the line of raw data.
        :return: the data ID of the current line of data
        """
        data_id_raw = self.next_id_text
        return data_id_raw.replace(' ','')

    def filter_tokens(self, line):
        """
        performs tokenization by separating all (important) tokens by space
        :param line: raw line of data from review
        :return: (string) line of review formed by space separated tokens
        """
        line.replace('.',' ')
        line.replace('(', ' ( ')
        line.replace('\n',' ')
        line = line.lower()
        line.replace('  ', ' ')
        split_words = line.split()

        for i in range(len(split_words)):
            word = split_words[i]
            word = self.cleanup_chars(len(word) - 1, word)
            word = self.cleanup_chars(0, word)
            split_words[i] = word

            self.special_delim('.', word, split_words, i)
            self.special_delim('-', word, split_words, i)
            self.special_delim('"', word, split_words, i)
            self.special_delim(',', word, split_words, i)
        return split_words

    def special_delim(self, delim, word, split_words, index):
        if delim in word:
            dot_split = word.split(delim)
            split_words[index] = dot_split[0]
            split_words.extend(dot_split[1:])

    def cleanup_chars(self, index, word):
        if index >= len(word):
            return word
        specified_char = word[index]
        if ord(specified_char) < ord('a') or ord(specified_char) > ord('z'):
            word = word[:index] + word[index + 1:]
        return word

    def close(self):
        self.datafile.close()
        return

    def read_labels(self):
        labels_dict = {}
        lines = self.datafile.read().splitlines()

        for line in lines:
            str_parts = line.split(' ')
            data_id = str_parts[0].replace(' ', '')
            genuine = str_parts[1].replace(' ', '')
            sentiment = str_parts[2].replace(' ', '')
            labels_dict[data_id] = (genuine, sentiment)

        self.close()
        return labels_dict
