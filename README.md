# Car Price Predictor

The **Car Price Predictor** is a machine learning web application that predicts the price of a car based on features such as **car model**, **company**, **year**, **kilometers driven**, and **fuel type**.

Built using **Flask**, this project leverages a trained **Linear Regression** model to provide accurate price estimates. It offers:

- A user-friendly input form  
- Instant price predictions  
- Live deployment for real-time use:  
  [https://car-price-predictor-owje.onrender.com](https://car-price-predictor-owje.onrender.com)

---

## Installation and Usage

To run this project locally, follow these steps:

### 1. Clone the Repository
```
$ git clone https://github.com/yourusername/CarPricePredictor.git
$ cd CarPricePredictor
```

### 2. Set Up a Virtual Environment

#### For Windows (PowerShell):
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Prepare Data and Model

Ensure the following files are present in the **project root directory**:

- `Cleaned_Car_data.csv`
- `LinearRegressionModel.pkl`

These files should match the **training data** and **model** used during development.

### 5. Run the Application
```
python app.py
```
