# Health Prediction Application

A simple AI/ML-based Health Prediction Application developed using Python, Streamlit, SQLite, and Scikit-learn.  
The application allows users to manage patient records and predict possible health risks based on blood test results.

---

# Features

✅ Add Patient Records  
✅ View Patient Records  
✅ Delete Patient Records  
✅ Health Risk Prediction using Machine Learning  
✅ SQLite Database Integration  
✅ Input Validation  
✅ Simple and User-Friendly Interface  
✅ Persistent Data Storage  

---

# Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- NumPy
- Scikit-learn

---

# Project Structure

```bash
health_prediction_app/
│
├── app.py
├── database.py
├── model.py
├── requirements.txt
├── patients.db
└── README.md
```

---

# Installation Guide

## Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## Step 2: Open Project Folder

```bash
cd health_prediction_app
```

---

## Step 3: Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### Mac/Linux

```bash
python3 -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

# Install Required Libraries

## Install Streamlit

```bash
pip install streamlit
```

## Install Pandas

```bash
pip install pandas
```

## Install Scikit-learn

```bash
pip install scikit-learn
```

## Install NumPy

```bash
pip install numpy
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Application Workflow

1. Enter patient details
2. Input blood test values:
   - Glucose
   - Haemoglobin
   - Cholesterol
3. System predicts possible health condition
4. Prediction is displayed in the Remarks field
5. Data is stored in SQLite database

---

# Input Validation

The application validates:

- Valid email format
- Date of birth cannot be future date
- Blood values must be numeric

---

# Machine Learning Model

The project uses a simple Random Forest Classifier from Scikit-learn to predict health risk categories based on blood test values.

Possible outputs include:

- Healthy
- Moderate Risk
- Diabetes Risk
- High Risk

---

# Database Used

SQLite database is used for persistent storage of patient records.

Database file:

```bash
patients.db
```


