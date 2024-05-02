import pandas as pd
import streamlit as st

def fetch_medical_history_by_name(patient_name):
    # Load the CSV data into a DataFrame
    data = pd.read_csv("patient.csv")
    # Sort the data by name and date
    data_sorted = data.sort_values(by=['Name', 'Date'])
    patient_data = data_sorted[data_sorted['Name'] == patient_name]
    return patient_data[['Date', 'Disease', 'Cured', 'Medications', 'Diagnosing_Doctor']]

# Streamlit UI
st.title('Patient Medical History')

# Input for patient name
patient_name = st.text_input('Enter Patient Name')

# Button to fetch medical history
if st.button('Fetch Medical History'):
    if patient_name:
        medical_history = fetch_medical_history_by_name(patient_name)
        if not medical_history.empty:
            st.success(f"Medical History for {patient_name}:")
            st.write(medical_history)
        else:
            st.warning("No medical history found for the provided patient name.")
    else:
        st.warning("Please enter a patient name.")