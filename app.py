# simple flask web app
from flask import Flask, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import Parallel, delayed
import joblib

app = Flask(__name__)


model = joblib.load('randomforestmodel.pkl') # best_rf
# Load the scaler
scaler = joblib.load('scaler.pkl') # best_rf_scaler


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
    
    data = pd.Series(data)
    data = pd.DataFrame([data], columns=data.index)

    categorical_cols = ['Health Conditions', 'Health Status', 'Activities']
    data_encoded = pd.get_dummies(data, columns=categorical_cols, dtype=int)
    data_encoded = data_encoded.reindex(columns=X_encoded.columns, fill_value=0)
    
    # Ensure the columns in prediction data match the training data
    """
        missing_cols = set(X_encoded.columns) - set(data_encoded.columns)
        for col in missing_cols:
            data_encoded[col] = 0
        data_encoded = data_encoded[X_encoded.columns]
    """
    
    custom_mapping = {'Unhealthy': 0, 'Unhealthy for sensitive groups': 1, 'Very unhealthy': 2, 'good': 3, 'moderate': 4}
    label_encoder_pm = LabelEncoder()
    label_encoder_pm.fit(list(custom_mapping.values()))
    data_encoded['pm_category'] = data_encoded['pm_category'].map(custom_mapping)
    # print(data_encoded.head())
    
    data_scaled = scaler.transform(data_encoded)
    predicted_label_encoded = model.predict(data_scaled)
    return predicted_label_encoded


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
    print(predicted_label_original)
    
    
    return render_template('predict.html', prediction=predicted_label_original[0])    



if __name__ == '__main__':
    app.run(debug=True)