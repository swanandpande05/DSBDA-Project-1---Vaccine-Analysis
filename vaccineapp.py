import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("COVID-19 Vaccination Analysis in India")

# Load dataset
df = pd.read_csv("covid_vaccine_statewise.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert columns
cols = [
    'First Dose Administered',
    'Second Dose Administered',
    'Male (Doses Administered)',
    'Female (Doses Administered)'
]

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.fillna(0)

# State-wise data
first_dose = df.groupby('State')['First Dose Administered'].max()
second_dose = df.groupby('State')['Second Dose Administered'].max()

# Show data
st.subheader("State-wise First Dose Vaccination")
st.write(first_dose)

st.subheader("State-wise Second Dose Vaccination")
st.write(second_dose)

# Gender data
male_total = df['Male (Doses Administered)'].max()
female_total = df['Female (Doses Administered)'].max()

st.subheader("Gender-wise Vaccination")
st.write(f"Male: {int(male_total)}")
st.write(f"Female: {int(female_total)}")

# Plot
st.subheader("Top 10 States by First Dose")
st.bar_chart(first_dose.sort_values(ascending=False).head(10))