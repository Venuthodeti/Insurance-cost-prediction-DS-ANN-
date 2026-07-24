# Insurance-cost-prediction-DS(ANN)
Insurance Cost Prediction using Artificial Neural Networks (ANN) and Deep Learning with TensorFlow/Keras. Built with Streamlit for an interactive web application.


# 🏥 Insurance Cost Prediction Using Deep Learning (ANN)

## 📌 Project Overview

This project predicts **medical insurance charges** based on an individual's personal and health-related information using an **Artificial Neural Network (ANN)** built with **TensorFlow/Keras**. An interactive **Streamlit** web application allows users to enter their details and receive an estimated insurance cost instantly.

---

## 🚀 Features

* Predicts medical insurance charges using a trained ANN model.
* Interactive and user-friendly Streamlit interface.
* Data preprocessing using Scikit-learn.
* Model saved using Keras (`.keras` format).
* Feature scaling using a saved scaler (`scaler.pkl`).
* Easy to run locally.

---

## 🛠️ Tech Stack

* **Python**
* **TensorFlow / Keras**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **Streamlit**
* **Joblib / Pickle**

---

## 📂 Project Structure

```text
Insurance-Cost-Prediction-Using-DL-ANN/
│── run.py                     # Streamlit application
│── insurance_model.keras      # Trained ANN model
│── scaler.pkl                 # Saved feature scaler
│── insurance.csv              # Dataset
│── requirements.txt           # Project dependencies
│── .gitignore
└── 1.Neural Network_Regression.ipynb
```

---

## 📊 Dataset

The project uses the **Medical Insurance Dataset**, which contains features such as:

* Age
* Sex
* BMI (Body Mass Index)
* Number of Children
* Smoker Status
* Region

Target Variable:

* **Insurance Charges**

---

## 🧠 Model

The prediction model is an **Artificial Neural Network (ANN)** developed using TensorFlow/Keras.

### Workflow

1. Data preprocessing
2. Feature encoding
3. Feature scaling
4. ANN model training
5. Model evaluation
6. Model saving
7. Streamlit deployment

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Venuthodeti/Insurance-cost-prediction-DS-ANN-.git
```

Move into the project folder:

```bash
cd Insurance-cost-prediction-DS-ANN-
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run run.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📸 Application Preview

Add screenshots of your Streamlit application here.

Example:

```
screenshots/home.png
screenshots/prediction.png
```

---

## 📈 Future Improvements

* Improve prediction accuracy through hyperparameter tuning.
* Deploy the application online.
* Add model comparison with other regression algorithms.
* Enhance UI/UX.
* Add input validation and error handling.

---

## 👨‍💻 Author

**Venu Thodeti**

* GitHub: https://github.com/Venuthodeti
* LinkedIn: *(Add your LinkedIn profile link here)*

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

