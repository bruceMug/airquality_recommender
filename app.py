# simple flask web app
from flask import Flask, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import Parallel, delayed
import joblib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    columns = ['age', 'Latitude', 'Longitude', 'pm_category',
       'Health Conditions_Asthma', 'Health Conditions_Chronic',
       'Health Conditions_High Blood Pressure', 'Health Conditions_None',
       'Health Conditions_Pneumonia', 'Health Status_Sick',
       'Activities_Running', 'Activities_Swimming', 'Activities_Walking']

    X_encoded = pd.DataFrame(columns=columns)
    # print(predict(20,'Asthma','Sick','Very unhealthy','Running',0.35319,32.46346))
    
    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)