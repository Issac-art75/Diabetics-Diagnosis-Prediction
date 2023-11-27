from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

def result(request):
    data = pd.read_csv(r"C:\Users\josep\Desktop\Diabetics_Prediction\diabetes.csv")

    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    model = LogisticRegression(solver='lbfgs', max_iter=150)
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result2 = ""
    if pred==[1]:
        result1 = "Positive"
    else:
        result1 = "Negative"

    return render(request,'predict.html', {"result2":result1})