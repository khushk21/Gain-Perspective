from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import warnings
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TreebankWordTokenizer
s1="Hi!you are very very annoying person.....you can fuck off pls bastard!!"
load_model=keras.models.load_model('../model/model',compile=True)
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    tokenizer = TreebankWordTokenizer()
    comment_tokens = tokenizer.tokenize(text)
    return comment_tokens

def remove_stopwords(text):
    stemmer=PorterStemmer()
    words=[]
    for word in text:
        if(word not in stopwords.words('english')):
            stem_word=stemmer.stem(word)
            words.append(stem_word)
    return words
def output_prediction(text):
    max_features = 22000
    tokenizer=Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(list(text))
    tokenized_train=tokenizer.texts_to_sequences(text)
    maxlen=200
    x_train=pad_sequences(tokenized_train,maxlen=maxlen)
    prediction=load_model.predict(x_train)
    return prediction
def performTweetAnalysis(text):
    cleaned_text_data = clean_text(text)
    preprocessed_data = remove_stopwords(cleaned_text_data)
    return output_prediction(preprocessed_data)
