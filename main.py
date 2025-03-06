import streamlit as st
import random
import string  

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

# Custom UI Styling
st.markdown(
    """
    <style>
        .main {background-color: #e3f2fd;}
        .stButton>button {background-color: #1e88e5; color: white; border-radius: 10px; padding: 10px 20px; font-size: 16px;}
        .stSlider>div {color: #1e88e5;}
        .stCheckbox>label {font-size: 16px; font-weight: bold; color: #1e88e5;}
        .password-box {background-color: #1e88e5; color: #fff; padding: 10px; border-radius: 10px; text-align: center; font-size: 20px; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center; color: #1e88e5;'>🔐 Password Generator</h1>", unsafe_allow_html=True)

length = st.slider("Select Password Length:", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Numbers")
use_special = st.checkbox("Include Special Characters")

generated_password = ""
if st.button("Generate Secure Password"):
    generated_password = generate_password(length, use_digits, use_special)
    
if generated_password:
    st.markdown(f"<div class='password-box'>{generated_password}</div>", unsafe_allow_html=True)