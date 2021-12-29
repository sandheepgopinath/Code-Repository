# Remove warnings
import warnings
warnings.filterwarnings('ignore')

#import matplotlib.pyplot as plt



import numpy as np
import pandas as pd
train = pd.read_csv("labeledTrainData.tsv", header=0, \
                    delimiter="\t", quoting=3)
# train.shape should be (25000,3)


test = pd.read_csv("testData.tsv", header=0, \
                    delimiter="\t", quoting=3)



import nltk
nltk.download(['stopwords', 'punkt', 'wordnet', 'averaged_perceptron_tagger'])


# import packages

import bs4 as bs
import nltk
from nltk.tokenize import sent_tokenize # tokenizes sentences
import re
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

eng_stopwords = stopwords.words('english')



from nltk.corpus import stopwords

eng_stopwords = stopwords.words('english')



# 1.
from nltk.corpus import stopwords


def review_cleaner(review):
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

    return(review)




num_reviews = len(train['review'])



review_clean_original = []

for i in range(0,num_reviews):
    if( (i+1)%500 == 0 ):
        # print progress
        print("Done with %d reviews" %(i+1))
    review_clean_original.append(review_cleaner(train['review'][i]))
temp=review_clean_original



## Example code BoW

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

sent1 = "cool students study cool data science"
sent2 = "to know data science study data science"

vect = CountVectorizer() #instantiate
vect2 = TfidfVectorizer()

sents = np.array([sent1,sent2])

vect.fit(sents);



from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics # for confusion matrix, accuracy score etc
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(\
    review_clean_original, train['sentiment'], random_state=0, test_size=.2)


# CountVectorizer can actucally handle a lot of the preprocessing for us
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000)



# Transform the text data to feature
# Only fit training data (to mimic real world)

vectorizer.fit(X_train)




import pickle
with open('count_vectorizer.pkl','wb') as file_out:
  pickle.dump(vectorizer,file_out)

with open('count_vectorizer.pkl', 'rb') as f:
    movieVect= pickle.load(f)



train_bag = vectorizer.transform(X_train) #transform to a feature matrix
test_bag = vectorizer.transform(X_test)

movieVect.transform([X_train[0]])


from sklearn.ensemble import RandomForestClassifier

## Initialize a Random Forest classifier with 50 trees
# hyperparameter n_estimators always set in instantiation

forest = RandomForestClassifier(n_estimators = 50)




# Fit the forest to the training set, using the bag of words as
# features and the sentiment labels as the target variable

forest = forest.fit(train_bag, y_train) # can take 20 seconds to run



import pickle
with open('classifier.pkl','wb') as file_out:
  pickle.dump(forest,file_out)

with open('classifier.pkl', 'rb') as f:
    forestt= pickle.load(f)
