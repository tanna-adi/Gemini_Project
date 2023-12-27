from dotenv import load_dotenv
load_dotenv() ## loading all the enviroment veriables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get responses

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

## initialize our steamlit app

st.set_page_config(page_title="Q&A Page")
st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

## when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.write(response)