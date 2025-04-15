from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

car = pd.read_csv('Cleaned_Car_data.csv')
logger.info("CSV loaded successfully")
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
logger.info("Model loaded successfully")

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique())
    fuel_types = sorted(car['fuel_type'].unique())
    company_models = {company: sorted(car[car['company'] == company]['name'].unique()) for company in companies}
    return render_template('index.html', companies=companies, car_models=car_models,
                           years=years, fuel_types=fuel_types, company_models=company_models)

@app.route('/predict', methods=['POST'])
def predict():
    car_model = request.form.get('car_models')
    company = request.form.get('company')
    year = int(request.form.get('year'))
    driven = int(request.form.get('kilo_driven'))
    fuel_type = request.form.get('fuel_type')

    input_data = pd.DataFrame({
        'name': [car_model],
        'company': [company],
        'year': [year],
        'kms_driven': [driven],
        'fuel_type': [fuel_type]
    })

    try:
        prediction = model.predict(input_data)
        logger.info("Prediction successful: %s", prediction)
        return str(np.round(prediction[0], 2))
    except Exception as e:
        logger.error("Prediction error: %s", str(e))
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)