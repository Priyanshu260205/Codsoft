from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('iris_classify_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from form
    features = [float(x) for x in request.form.values()]
    final_input = np.array([features])
    
    prediction = model.predict(final_input)
    
    # Target names
    classes = ['Setosa', 'Versicolor', 'Virginica']
    result = classes[prediction[0]]
    
    return render_template('index.html', prediction_text=f'The Iris flower is likely: {result}')

if __name__ == '__main__':
    app.run(debug=True)
