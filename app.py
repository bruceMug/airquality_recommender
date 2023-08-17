# simple flask web app
from flask import Flask, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import Parallel, delayed
import joblib

app = Flask(__name__)

def get_recommendation(user_details, X_encoded):
    age, health_condition, health_status, pm_category, activities, latitude, longitude = user_details
    data = {'age': age,
          'Health Conditions': health_condition,
          'Health Status': health_status,
          'Activities': activities,
          'Latitude': latitude,
          'Longitude':longitude,
          'pm_category': pm_category
          }
    return True


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
    
    custom_mapping_inverse_recommendation = {0: 'Avoid all physical outdoor activities ❌',
                                             1: 'Avoid prolonged/heavy outdoor exertion ❌',
                                             2: 'Good day to be active outside ☀️',
                                             3: 'Great day to be active outside 🌞',
                                             4: 'Reduce prolonged or heavy outdoor exertion ⚠️',
                                             5: 'Take more breaks during outdoor activities ⏸',
                                             6: 'Keep quick relief medicine handy 💊',
                                             7: 'Reschedule for when air quality is better 📅'}

    # predicted_label_encoded = [6]
    age = 40
    health_condition = 'Chronic'
    health_status = 'Sick'
    pm_category = 'Very unhealthy'
    activities = 'Walking'
    latitude = 0.35319
    longitude = 32.46346
    
    user_details = [age, health_condition, health_status, pm_category, activities, latitude, longitude]
    predicted_label_encoded = get_recommendation(user_details, X_encoded)
    
    predicted_label_original = [custom_mapping_inverse_recommendation[label] for label in predicted_label_encoded]
    
    
    return render_template('predict.html', prediction=predicted_label_original[0])    


if __name__ == '__main__':
    app.run(debug=True)