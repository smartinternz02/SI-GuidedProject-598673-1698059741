import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, render_template, url_for, request
import pickle
app = Flask(__name__)


def decisionTreeClassifier(arr):
    # data = pd.read_csv('car_data.csv')
    # data['Gender'].replace(['Male', 'Female'],
    #                        [0, 1], inplace=True)
    # x = data[['Gender', 'Age', 'AnnualSalary']]
    # y = data['Purchased']
    # clf = DecisionTreeClassifier()
    # clf.fit(x, y)
    # y_pred = clf.predict(arr)
    # if y_pred == 1:
    #     return 'The Customer is predicted to purchase a car'
    # return 'The Customer is predicted to not purchase a car'
    model = pickle.load(open("model.pkl", "rb"))
    pred = model.predict(arr)
    if pred[0] == 1:
        return 'The Customer is predicted to purchase a car'
    return 'The Customer is predicted to not purchase a car'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        age = int(request.form['age'])
        annualSal = int(request.form['annualSal'])
        testData = [[gender, age, annualSal]]
        resultText = decisionTreeClassifier(testData)
        return render_template('result.html', resultText=resultText)
    else:
        return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
