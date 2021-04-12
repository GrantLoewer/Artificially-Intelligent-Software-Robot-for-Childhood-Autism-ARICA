import csv
import nltk
import string
import numpy as np
from nltk.corpus import stopwords
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
nltk.download('stopwords')

#ARICA introduces herself
print("Hello my name is ARICA!")
print("")
print("")
print("My face is materializing, please wait!")
print("")
print("")

#sentences and whether they display positivity or negativity
sentences = []
sentiments = []

#dataset of amazon product reviews
with open('amazon_cells_labelled.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        sentences.append(i[0])
        sentiments.append(i[1])

#dataset of imdb movie reviews
with open('imdb_labelled.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        sentences.append(i[0])
        sentiments.append(i[1])

#dataset of yelp reviews
with open('yelp_labelled.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        sentences.append(i[0])
        sentiments.append(i[1])

x = sentences
y = sentiments

def processing_text(text):
    #get stopwords
    stop_words = set(stopwords.words('english'))
    #tokenize sentence
    words = text.split()
    #remove the stopwords
    text_without_stopwords = " ".join([word for word in text.lower().split() if word not in stop_words])
    #get punctuations
    punctuation_marks = set(string.punctuation)
    # remove punctuation marks
    for symbol in punctuation_marks:
        if symbol in text_without_stopwords:
            text_without_stopwords = text_without_stopwords.replace(symbol, "")
    # remove numbers
    for num in range(10):
        if str(num) in text:
            text_without_stopwords = text_without_stopwords.replace(str(num), "")

    return text_without_stopwords.split()

'''
#test to see if databases are there
for i in range(0,5):
    test = processing_text(x[i])
    print(x[i])
    print(test)
'''

#build the vocab
iterate = list(x)
vocab = CountVectorizer(analyzer=processing_text).fit(iterate)

#document-term matrix from documents
vocab_matrix = vocab.transform(iterate)

#split to have 80% train and 20% test data
X_train, x_test, Y_train, y_test = train_test_split(vocab_matrix, y, test_size=0.20)

sentiment_model = MultinomialNB().fit(X_train, Y_train)
accuracy = sentiment_model.score(x_test, y_test)
#print ("Accuracy: ", accuracy * 100)
#prediction = sentiment_model.predict(x_test)


#Didn't work with mutltiple labels
'''
#words and the emotions they display
words = []
emotions = []

with open('NRC-Emotion-Lexicon-v0.92.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        words.append(i[0])
        i.pop(0)
        emotions.append(i)

x_dict = words
y_dict = emotions


#build the vocab
iterate_emo = list(x_dict)
#vocab_emo = CountVectorizer(analyzer=processing_text).fit(iterate_emo)
vocab_emo = []
for i in iterate_emo:
    vocab_emo.append(processing_text(i))

#document-term matrix from documents
#vocab_matrix_emo = vocab_emo.transform(iterate_emo)

#split to have 80% train and 20% test data
X_train_emo, x_test_emo, Y_train_emo, y_test_emo = train_test_split(vocab_emo, y_dict, test_size=0.20)

print(x_test_emo)
print(y_test_emo)
emotions_model = MultinomialNB().fit(X_train_emo, Y_train_emo)
accuracy_emo = emotions_model.score(x_test_emo, y_test_emo)

print ("Accuracy: ", accuracy_emo * 100)
prediction_emo = emotions_model.predict(x_test_emo)
'''

#words and the emotions they display
words = []
emotions = []

with open('NRC-Emotion-Lexicon-v0.92.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        words.append(i[0])
        emotions.append(i[11])

x_dict = words
y_dict = emotions

#build the vocab
iterate_emo = list(x_dict)
vocab_emo = CountVectorizer().fit(iterate_emo)
'''
vocab_emo = []
for i in iterate_emo:
    vocab_emo.append(processing_text(i))
'''

#document-term matrix from documents
vocab_matrix_emo = vocab_emo.transform(iterate_emo)

#split to have 80% train and 20% test data
X_train_emo, x_test_emo, Y_train_emo, y_test_emo = train_test_split(vocab_matrix_emo, y_dict, test_size=0.20)

emotions_model = MultinomialNB().fit(X_train_emo, Y_train_emo)
accuracy_emo = emotions_model.score(x_test_emo, y_test_emo)

#print ("Accuracy: ", accuracy_emo * 100)
#prediction_emo = emotions_model.predict(x_test_emo)


#predict the emotion of the user's inputs
user_sentence = 'happy'
user_sentence_vocab = CountVectorizer(analyzer=processing_text,vocabulary=vocab_emo.vocabulary_)
user_sentence_vocab_matrix = user_sentence_vocab.transform(user_sentence)
user_prediction = emotions_model.predict(user_sentence_vocab_matrix)
#print("Predicted: ", user_sentence, "as", user_prediction)



'''
#predict if the user's input is positive or negative
user_sentence = ['This was the best product I have ever bought, I love it!']
user_sentence_vocab = CountVectorizer(analyzer=processing_text,vocabulary=vocab.vocabulary_)
user_sentence_vocab_matrix = user_sentence_vocab.transform(user_sentence)
user_prediction = sentiment_model.predict(user_sentence_vocab_matrix)

print("Predicted: ", user_sentence, "as", user_prediction)

if user_prediction == '0':
    #This is a positive sentence
    pass
else:
    #This is a negative sentence
    pass
'''
