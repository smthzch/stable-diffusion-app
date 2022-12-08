from fastapi import FastAPI
from fastapi.responses import Response
from model import StableDiffusion
import io

model = StableDiffusion("model")

app = FastAPI()

@app.get("/")
async def root(prompt: str = "fractal goats"):
    image = model(prompt)

    output = io.BytesIO()
    image.save(output, format='JPEG')

    response = Response(output.getvalue(), media_type="image/jpg")
    return response
