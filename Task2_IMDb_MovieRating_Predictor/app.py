from flask import Flask, render_template, request
import joblib
import pandas as pd

model = joblib.load("movie_rating_model.pkl")
model_columns = joblib.load("model_columns1.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        data = pd.DataFrame([[
            int(request.form['year']),
            int(request.form['duration']),
            request.form['genre'],
            request.form['director'],
            request.form['actor1'],
            request.form['actor2'],
            request.form['actor3']
        ]], columns=['Year', 'Duration', 'Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3'])

        # Encode
        input_encoded = pd.get_dummies(data).reindex(columns=model_columns, fill_value=0)
        prediction = round(model.predict(input_encoded)[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)