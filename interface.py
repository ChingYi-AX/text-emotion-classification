import ktrain


def predict():
    print('\033[95m' + "- Hi, please enter a sentence or  paragraph, our model will predict emotion. Type quit to stop "
                       "prediction." + '\033[0m')
    user_input = input()

    print('\033[95m' + "- Loading existing emotion model..., please wait for a while :)" + '\033[0m')
    reloaded_predictor = ktrain.load_predictor('checkpoints/')

    while "quit" not in user_input.lower():
        if isinstance(user_input, str):
            predicted_label = reloaded_predictor.predict(user_input)
            print("\033[94m- The emotion of the above sentence is: \033[4m{}\033[0m".format(predicted_label))
        else:
            print('\033[0m91' + "- Please check the your input, you can enter for exammple: I love you" + '\033[0m')
        print('\033[95m' + "- Please enter other sentences or paragraphs for next round of prediction ;)" + '\033[0m')
        user_input = input()
    print('\033[93m' + "See you!" + '\033[0m')


predict()
