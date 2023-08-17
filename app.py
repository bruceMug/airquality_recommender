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


if __name__ == '__main__':
    app.run(debug=True)