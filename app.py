import streamlit as st
import pandas as pd
from datetime import date
import re

from database import (
    add_patient,
    get_patients,
    update_patient,
    delete_patient
)

from model import predict_health

st.title("Health Prediction Application")

menu = ["Add Patient", "View Patients"]
choice = st.sidebar.selectbox("Menu", menu)

# EMAIL VALIDATION
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# ADD PATIENT
if choice == "Add Patient":

    st.subheader("Add New Patient")

    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    email = st.text_input("Email Address")

    glucose = st.number_input("Glucose")
    haemoglobin = st.number_input("Haemoglobin")
    cholesterol = st.number_input("Cholesterol")

    if st.button("Predict & Save"):

        # VALIDATION
        if not valid_email(email):
            st.error("Invalid Email Format")

        elif dob > date.today():
            st.error("Date of Birth cannot be future date")

        else:
            remarks = predict_health(
                glucose,
                haemoglobin,
                cholesterol
            )

            add_patient(
                name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success(f"Patient Saved Successfully")
            st.info(f"Prediction Result: {remarks}")

# VIEW PATIENTS
elif choice == "View Patients":

    st.subheader("Patient Records")

    data = get_patients()

    df = pd.DataFrame(data, columns=[
        "ID",
        "Name",
        "DOB",
        "Email",
        "Glucose",
        "Haemoglobin",
        "Cholesterol",
        "Remarks"
    ])

    st.dataframe(df)

    st.subheader("Delete Patient")

    patient_id = st.number_input("Enter Patient ID", step=1)

    if st.button("Delete"):
        delete_patient(patient_id)
        st.success("Patient Deleted Successfully")