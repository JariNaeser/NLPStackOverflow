import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn import preprocessing

labels_list_training = []
text_list_training = []
labels_list_test = []
text_list_test = []

with open('filtered_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row    

    #Add in training only the first half of the rows in the csv, then in test the next half
    for i, row in enumerate(csv_reader):
        if i < 2000:
            labels_list_training.append(row[0])
            text_list_training.append(row[1])
        else:
            labels_list_test.append(row[0])
            text_list_test.append(row[1])

# Conversione dei testi in features (conteggio parole)
vectorizer = CountVectorizer()
training_features = vectorizer.fit_transform(text_list_training)
test_features = vectorizer.transform(text_list_test)

# Training 
classifier = MultinomialNB()
classifier.fit(training_features, labels_list_training)

# Test
predictions = classifier.predict(test_features)

target_names = ['java', 'python', 'c', 'javascript']
print(classification_report(labels_list_test, predictions, target_names=target_names))

print("------------------------------------------------------")
# Training 
classifier = LogisticRegression()
classifier.fit(training_features, labels_list_training)

# Test
predictions = classifier.predict(test_features)

target_names = ['java', 'python', 'c', 'javascript']
print(classification_report(labels_list_test, predictions, target_names=target_names))