from dotenv import load_dotenv
load_dotenv() ## loading all the enviroment veriables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro vision model and get responses

model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input != "":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

## initialize our steamlit app

st.set_page_config(page_title="Gemini vision Page")
st.header("Gemini Vision Application")

input=st.text_input("Input: ",key="input")

uploaded_file = st.file_uploader("Choose an image..", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image",use_column_width=True)
submit = st.button("tell me about image")

## if sumbit is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)