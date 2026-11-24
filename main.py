import streamlit as st
import pandas as pd

st.title("Personal Expense Tracker")

date = st.date_input("Date")
category = st.selectbox(
    "Category",
    ["Food", "Travel", "Shopping", "Education", "Other"]
)
amount = st.number_input("Amount", min_value=0.0)
description = st.text_input("Description")

if st.button("Add Expense"):
    if amount > 0:
        data = {
            "Date": [date],
            "Category": [category],
            "Amount": [amount],
            "Description": [description]
        }

        df = pd.DataFrame(data)
        df.to_csv("expenses.csv", index=False)
        st.success("Expense added successfully!")
