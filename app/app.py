import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/customer_churn_sample.csv")

st.title("📊 Customer Churn Dashboard")

# Show data preview
st.subheader("Customer Data")
st.dataframe(df)

# Churn distribution
st.subheader("Churn Distribution")
churn_counts = df["Churn"].value_counts()
st.bar_chart(churn_counts)

# Monthly Charges by Churn
st.subheader("Monthly Charges by Churn")
fig, ax = plt.subplots()
df.boxplot(column="MonthlyCharges", by="Churn", ax=ax)
plt.title("Monthly Charges by Churn")
plt.suptitle("")  # Hide automatic title
st.pyplot(fig)

# Average Tenure by Gender
st.subheader("Average Tenure by Gender")
avg_tenure = df.groupby("Gender")["Tenure"].mean()
st.bar_chart(avg_tenure)
