from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Q&A Demo",
    page_icon="📊",
    layout="centered"
)

# --- Streamlit UI ---
st.header("Gemini LLM Application")

# Input text field
user_text = st.text_input("Enter your question:", key="input")

# Submit button
if st.button("Ask the Question"):
    if user_text.strip():  # Ensure input is not empty
        response = get_gemini_response(user_text)
        st.subheader("Response:")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")
