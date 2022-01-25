import os
import argparse
import ktrain
from ktrain import text
from sklearn.model_selection import train_test_split
from data_preprocess.data_process import DataReader

lookup_table = {'noemo': 0, 'joy': 1, 'fear': 2,
                'sadness': 3, 'surprise': 4, 'anger': 5,
                'disgust': 6, 'love': 7, 'shame': 8,
                'guilt': 9, 'trust': 10, 'anticipation': 11
                }
class_names = ['noemo', 'joy', 'fear', 'sadness', 'surprise', 'anger',
               'disgust', 'love' 'shame', 'guilt', 'trust', 'anticipation']


def _get_train_test_set(data, split=0.8):
    split_point = int(data.shape[0] * split)
    train_data, test_data = train_test_split(data[:split_point], test_size=0.1,
                                             stratify=data[['Emotion']][:split_point])
    X_train, Y_train = train_data.Text.tolist(), train_data.Emotion.tolist()
    X_test, Y_test = test_data.Text.tolist(), test_data.Emotion.tolist()
    class_names = list(set(Y_train))

    (x_train, y_train), (x_test, y_test), preproc \
        = text.texts_from_array(
        x_train=X_train,
        y_train=Y_train,
        x_test=X_test,
        y_test=Y_test,
        class_names=class_names,
        preprocess_mode='bert',
        maxlen=100,
        max_features=35000)
    return (x_train, y_train), (x_test, y_test), preproc


def train(epoch, train_set, test_set, preproc, rebuild_model=False):
    (x_train, y_train) = train_set
    (x_test, y_test) = test_set
    # check if we have existed model
    print("--------Start fine-tuning BERT pre-trained model with our data--------")
    model = text.text_classifier('bert', train_data=(x_train, y_train), preproc=preproc)
    learner = ktrain.get_learner(model, train_data=(x_train, y_train), val_data=(x_test, y_test), batch_size=2)
    learner.fit_onecycle(lr=2e-5, epochs=epoch, checkpoint_folder='/tmp/models')
    learner.validate(val_data=(x_test, y_test))
    predictor = ktrain.get_predictor(learner.model, preproc)
    predictor.save('/tmp/models')

    # for each class evaluate on precision, recall, f1-score with support(number of datapoint)
    # load and save predictor for later use

    return predictor


def main(epoch, data_path, rebuild_model=False):
    # read data
    data_reader = DataReader(file_path=data_path)
    data = data_reader.get_data_label(multi_label=False)
    print(os.path.exists('checkpoints/'), rebuild_model)

    if os.path.exists('checkpoints/') and rebuild_model == 'False':
        # used existed emotion model which already fine-tuned on 12 emotion dataset
        print("--------Used existed model--------")
        reloaded_predictor = ktrain.load_predictor('checkpoints/')
        predictor = reloaded_predictor
    else:
        # prepare and split data
        # load bert model and start training
        (x_train, y_train), (x_test, y_test), preproc = _get_train_test_set(data=data)
        predictor = train(epoch=epoch, train_set=(x_train, y_train), test_set=(x_test, y_test), preproc=preproc,
                          rebuild_model=rebuild_model)

    # evaluation/predict for some real data
    print("------Display examples of predicted results------")
    predict_data = data[20:]
    text_inputs = predict_data.Text.tolist()
    predicted_labels = predictor.predict(text_inputs)
    gold_labels = predict_data.Emotion.tolist()
    for text_input, predicted_label, gold_label in zip(text_inputs, predicted_labels, gold_labels):
        print("Input Text: {}\nPredicted Label --> {} / \tGround Truth Label --> {}".format(text_input, predicted_label,
                                                                                            gold_label))


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--epoch', dest='epoch', type=int)
    arg_parser.add_argument('--date_path', dest='f', type=str)
    arg_parser.add_argument('--rebuild_model', dest='rebuild', type=str)
    args = arg_parser.parse_args()

    main(epoch=args.epoch, data_path=args.f, rebuild_model=args.rebuild)

