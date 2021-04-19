import numpy as np
from flask import Flask, request, render_template
from joblib import load
from pathlib import Path
import os
from sklearn.preprocessing import  OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
#PROJECT_ROOT = Path(os.path.abspath('')).resolve().parents[0]
app = Flask(__name__)  # Initialize the flask App

rules=pd.read_csv(r'C:\Users\Utilizador\OneDrive - NOVAIMS\2º Semester\Business Cases with Data Science\PROJETOS\Business_Case_3\App\Rules.csv',index_col=0)
def recommender_system(prod):
    y = rules.loc[rules["antecedents"]==("'"+ prod + "'")]

    if len(y)!=0:
        aux = "Recommended product: " + y["consequents"].values[0]
        return aux
    else:
        return 'No recommendation available'

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        product =str(request.form['product'])
        output= recommender_system(product)
        return render_template('index.html', prediction_text=output)

if __name__ == '__main__':
	app.run(debug=True)