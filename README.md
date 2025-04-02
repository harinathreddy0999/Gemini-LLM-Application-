# Gemini Streamlit Applications

This repository contains three different Streamlit applications utilizing Google's Gemini models for text and vision-based interactions.

## 1️⃣ Gemini Q&A Demo
A simple Streamlit app that allows users to ask questions and get responses from the `gemini-2.5-pro-exp-03-25` model.

### Features:
- Accepts text-based questions.
- Returns responses from the Gemini model.

### Installation & Running:
```sh
pip install -r requirements.txt
streamlit run qa_demo.py
```

## 2️⃣ Gemini Vision Q&A
An enhanced application that allows users to provide text and images as input to receive AI-generated responses.

### Features:
- Accepts both text and image inputs.
- Utilizes the `gemini-1.5-pro-latest` model.
- Handles chat history.

### Installation & Running:
```sh
pip install -r requirements.txt
streamlit run vision_qa.py
```

## 3️⃣ Gemini Vision Chatbot
A chatbot implementation that maintains a chat history and allows interactions using both text and images.

### Features:
- Stores chat history using `st.session_state`.
- Allows uploading images and asking questions.
- Uses `gemini-1.5-pro-latest` for AI-powered responses.

### Installation & Running:
```sh
pip install -r requirements.txt
streamlit run chatbot.py
```

## Requirements
Ensure you have the required dependencies installed:
```sh
pip install streamlit google-generativeai pillow python-dotenv
```

## Environment Variables
Create a `.env` file and add your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

## License
This project is licensed under the MIT License.
