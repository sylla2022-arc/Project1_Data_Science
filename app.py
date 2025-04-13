import os
import sys
import io
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


obj_root = os.path.abspath(os.path.join(os.getcwd(), '../..'))
sys.path.append(obj_root)

from flask import Flask, render_template, request
import numpy as np
import pandas as pd 
from src.Project1_Data_Science.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET'])  # root to train pipeline
def training():
    print("Training started")

    # ✅ Ajout de encoding='utf-8'
    try:
        result = subprocess.run(
            ['python', 'main.py'],
            capture_output=True,
            text=True,
            encoding='utf-8'  # 🔥 ligne importante
        )
        
        if result.returncode == 0:
            # Affiche uniquement dans le terminal
            print("Training completed successfully!")
            print(f"Output: {result.stdout}")  # Affiche le stdout dans le terminal
            return "Training completed successfully!", 200  # Pas d'output dans la réponse HTTP
        else:
            # Affiche uniquement dans le terminal
            print(f"Error during training: {result.stderr}")
            return "Training failed!", 500  # Pas d'error details dans la réponse HTTP
    except Exception as e:
        # Affiche uniquement dans le terminal
        print(f"An error occurred: {str(e)}")
        return f"Training failed! Error: {str(e)}", 500  # Pas de détails dans la réponse HTTP



@app.route('/predict', methods=['POST', 'GET']) # root to web ui
def index():
    if request.method == 'POST':
        print("DEBUG - Form data received:", request.form)
        # Get the form data
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])    
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            ph = float(request.form['ph'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data =[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
                   free_sulfur_dioxide, total_sulfur_dioxide, density, ph, sulphates, 
                   alcohol]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)
            print(predict)

            # Formater la prédiction (arrondir à 2 décimales)
            result = round(float(predict[0]), 2)

            # Passer la valeur formatée à la template
            return render_template('results.html', prediction=result)

        except Exception as e:
            print(e)
            return "Error in prediction. Please check the input values."
        
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True, port=5000) # run the flask app on port 5000