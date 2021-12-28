import bs4 as bs
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import warnings
warnings.filterwarnings('ignore')

class analyse:
    def __init__(self,review):
        '''
        Clean and preprocess a review.

        1. Remove HTML tags
        2. Use regex to remove all special characters (only keep letters)
        3. Make strings to lower case and tokenize / word split reviews
        4. Remove English stopwords
        5. Rejoin to one string
        '''

        #1. Remove HTML tags
        review = bs.BeautifulSoup(review).text

        #2. Use regex to find emoticons
        emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', review)

        #3. Remove punctuation
        review = re.sub("[^a-zA-Z]", " ",review)

        #4. Tokenize into words (all lower case)
        review = review.lower().split()

        #5. Remove stopwords
        eng_stopwords = set(stopwords.words("english"))
        review = [w for w in review if not w in eng_stopwords]

        #6. Join the review to one sentence
        review = ' '.join(review+emoticons)
        # add emoticons to the end

        self.review=review  
        self.cv_model=None
        self.model=None

        self.count_vectorizer()
        self.preprocess()


    def count_vectorizer(self):
        ''' Function to load count vectorizer which was trained earlier. 
        If the file is not found, it will throw an error'''
        try:
            with open ('count_vectorizer.pkl','rb') as f:
                self.cv_model=pickle.load(f)
                self.review=self.cv_model.transform([self.review])
        except:
            print('Count Vectorizer file missing')

    def preprocess(self):
        ''' Loads the sentiment analysis model, completes the preprocessing and does the prediction
        '''
        with open('classifier.pkl', 'rb') as f:
            self.model= pickle.load(f)

        prediction=self.model.predict(self.review)
        if prediction[0]==1:
            self.prediction='Positive'
        else:
            self.prediction='Negative'

