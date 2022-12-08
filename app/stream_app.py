import streamlit as st
from model import StableDiffusion

model = StableDiffusion("model")

st.text_input("What do you want to see?", key="prompt", value="fractal goat")

st.image(
    model(st.session_state.prompt) 
)
