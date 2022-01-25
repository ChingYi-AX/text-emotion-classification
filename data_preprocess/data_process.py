import json
import os
import pandas as pd


def valid_json(json_file):
    try:
        json.loads(json_file)
    except ValueError as error:
        return False
    return True


class DataReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def _read_data(self):
        """The default data is in excel or json format"""
        file_exist = os.path.exists(self.file_path)
        if valid_json(self.file_path) and file_exist:
            return pd.readjson(self.file_path)
        elif file_exist:
            return pd.read_table(self.file_path, error_bad_lines=False, sep="\t")
        else:
            print('Please use valid json or excel file and check the file path.')

    def show_data_statistics(self, df):
        count = df['Corpora'].value_counts()
        print("--------Number of data of each corpora in the unified corpora--------\n{}".format(count))
        emotion = df['Emotion'].value_counts()
        print("--------Number of emotion type in the unified corpora--------\n{}".format(emotion))

    def get_data_label(self, multi_label=False):
        df = self._read_data()
        df.columns = ['ID', 'Corpora', 'Text', 'Emotion']
        self.show_data_statistics(df)
        # extract single and multiple label respectively
        data = df[['Text', 'Emotion']]
        data = data.dropna()

        data_multiple_label = data[[(len(str(x).split(",")) > 1) for x in data['Emotion']]]
        data_single_label = data[
            [(len(str(x).split(",")) < 2) for x in data['Emotion']]]  # remain 205459 samples, which is single label
        print("Number of mutiple labels: {}\nData examples:{}\n".format(data_multiple_label.shape[0],
                                                                        data_multiple_label.head(10)))
        print("Number of single labels: {}\nData examples:{}\n".format(data_single_label.shape[0],
                                                                       data_single_label.head(15)))
        if not multi_label:
            data = data_single_label
        return data

