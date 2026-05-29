from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample training data
X = np.array([
    [90, 13, 180],
    [150, 10, 250],
    [120, 12, 220],
    [80, 14, 170],
    [200, 9, 300]
])

y = np.array([
    "Healthy",
    "Diabetes Risk",
    "Moderate Risk",
    "Healthy",
    "High Risk"
])

model = RandomForestClassifier()
model.fit(X, y)


def predict_health(glucose, haemoglobin, cholesterol):
    prediction = model.predict([[glucose, haemoglobin, cholesterol]])
    return prediction[0]