from fastapi import FastAPI
from fastapi.responses import Response
import io
from PIL import Image as im

# load pretrained model
from diffusers import StableDiffusionPipeline
import torch

model_id = "model" # "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to(device)

# start server
app = FastAPI()

@app.get("/")
async def root(prompt: str = "fractal goats"):
    image = pipe(prompt).images[0]  

    output = io.BytesIO()
    image.save(output, format='JPEG')

    response = Response(output.getvalue(), media_type="image/jpg")
    return response
