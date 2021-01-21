import pickle
import numpy as np

class Sentiment():
    def __init__(self):
        #loading the pre-trained model from the Jupyter Notebook
        self.filename = 'sentiment_model_pipeline.sav'
        loaded_model = pickle.load(open(self.filename, 'rb'))

        #Requesting a review input
        input_str = input("Enter a review: ")

        result = loaded_model.predict([input_str])

        print("\nProcessing ...\n")
        
        #interpreting the result
        for sentiments in result:
            if sentiments == 0:
                print("Review: Negative")
            elif sentiments == 1:
                print("Review: Positive")
            else:
                print("Invalid")


if __name__ == '__main__':
    sent = Sentiment()
