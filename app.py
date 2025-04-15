from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

car = pd.read_csv('Cleaned_Car_data.csv')
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

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
    
    # Note: 'Price' column exists but isn't used here; adjust if your model expects it
    prediction = model.predict(pd.DataFrame(
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
        data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)
    ))
    
    print("Prediction:", prediction)
    return str(np.round(prediction[0], 2))

if __name__ == "__main__":
    app.run(debug=True)