
from sklearn.externals import joblib
import numpy as np
import json


load_clf = joblib.load("NBmodel.pkl")

with open("spam.text",'r') as json_file:
	dictionary = json.load(json_file)

def predictMail(mail):
	predict_me  = []
	
	mail = mail.split(" ")

	data = []
		
	for entry in dictionary:
		data.append(mail.count(entry[0]))
	predict_me.append(data)
		
	predict = load_clf.predict(predict_me)


	print(["Spam","Not Spam"][predict[0]])

mail = input()
predictMail(mail)
