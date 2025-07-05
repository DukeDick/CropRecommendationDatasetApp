from flask import Flask, request, render_template
import numpy as np
import pickle

# Load trained Random Forest model
model = pickle.load(open('RandomForest.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get form inputs
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])

        # Put input into correct format
        input_data = np.array([[N, P, K, temp, humidity, ph, rainfall]])

        # Predict crop directly
        prediction = model.predict(input_data)[0]  # Output will be a string like 'rice'

        result = f"🌱 {prediction} is the best crop to be cultivated right there."

    except Exception as e:
        result = f"❌ Error: {str(e)}"

    return render_template("index.html", result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
