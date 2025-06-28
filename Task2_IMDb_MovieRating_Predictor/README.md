# 🎬 Movie Rating Prediction App

A machine learning-powered web app built with **Flask** that predicts IMDb movie ratings based on features like **genre**, **director**, and **actors**.

This project uses the **IMDb Movies India** dataset from Kaggle and showcases data preprocessing, model training, and deployment through a clean web interface.

---

## 🚀 Features

- 🔍 Predict IMDb rating using movie metadata
- 🎨 Clean, responsive user interface (HTML + CSS)
- ⚙️ Flask-powered backend
- 📦 Pretrained model with `.pkl` files
- 🧠 Machine Learning using Random Forest Regressor

---

## 🗂️ Project Structure

movie-rating-app/
├── app.py # Flask web application
├── IMDB_MovieRating.ipynb # Jupyter notebook (model training)
├── IMDb Movies India.csv # Raw dataset
├── model_columns.pkl # Feature columns used in the model
├── movie_rating_model.pkl # Trained ML model
├── requirements.txt # Python dependencies
├── .gitignore
├── templates/
│ └── index.html # Web app HTML
├── static/
│ └── style.css # CSS styling
└── README.md


---

## 🧪 Sample Input

Year: 2015
Duration: 120
Genre: Action, Thriller
Director: Rohit Shetty
Actor 1: Ajay Devgn
Actor 2: Kareena Kapoor
Actor 3: Anupam Kher


✅ **Predicted IMDb Rating:** _e.g.,_ `5.14`

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Priyanshu260205/Codsoft/tree/main/Task2_IMDb_MovieRating_Predictor
cd Codsoft/tree/main/Task2_IMDb_MovieRating_Predictor
