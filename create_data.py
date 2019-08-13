import os
from collections import Counter
from sklearn.model_selection import train_test_split as tts
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import numpy as np
import json

def create_param():

	direct = "emails/"
	email_list = [direct+email for email in os.listdir(direct)]
	
	word_list = []

	c = len(email_list)

	for email in email_list:
		with open(email, encoding="latin-1") as datafile:
			blob = datafile.read()
			words = blob.split(" ")

			for word in words:
				word_list.append(word)

	for i in range(len(word_list)):
		if not word_list[i].isalpha():
			word_list[i] = ""


	dictionary = Counter(word_list)
	del(dictionary[""])

	return dictionary.most_common(3000)




def create_df(dictionary):
	print("Hell0")
	direct = "emails/"
	email_list = [direct+email for email in os.listdir(direct)]
	
	word_list = []

	c = len(email_list)
	feature_set = []
	for email in email_list:
		with open(email, encoding="latin-1") as datafile:
			blob = datafile.read()
			words = blob.split(" ")


			data = []
			for entry in dictionary:
				data.append(words.count(entry[0]))
			feature_set.append(data)
		print(c)
		c-=1


	labels = []
	for email in email_list:
		if("spam" in email):
			labels.append(0)
		else:
			labels.append(1)

	print(len(labels))
	print(len(feature_set))
	return feature_set,labels



dictionary = create_param()
dataset,labels = create_df(dictionary)

X_train,X_test,y_train,y_test = tts(dataset,labels,test_size = 0.20)

# clf = MultinomialNB()
# clf.fit(X_train,y_train)

len(dataset)
len(labels)

load_clf = joblib.load("NBmodel.pkl")

with open("spam.text",'r') as json_file:
	dictionary = json.load(json_file)

preds = load_clf.predict(X_test)
print(accuracy_score(y_test,preds))


# joblib.dump(clf,"NBmodel.pkl")

# with open("spam.text",'w') as json_file:
# 	json = json.dumps(dictionary,json_file)