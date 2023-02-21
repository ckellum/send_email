import streamlit as st
import pandas
from send_email import send_email


st.header("Contact Us")
topics = pandas.read_csv("topics.csv")

with st.form(key="my_form"):
    email_address = st.text_input("Email address")
    selection = st.selectbox("Topic", topics)
    message = st.text_area("Message")
    message = f"""Subject: New email from {email_address}
    
From: {email_address}\n
Topic: {selection}
{message}"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)



