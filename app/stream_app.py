import streamlit as st
import io
from PIL import Image as im

# load pretrained model
from diffusers import StableDiffusionPipeline
import torch

model_id = "model" # "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to(device)

st.text_input("What do you want to see?", key="prompt", value="fractal goat")

image = pipe(st.session_state.prompt).images[0]  
st.image(image)
