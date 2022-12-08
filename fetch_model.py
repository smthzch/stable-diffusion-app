
from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"

if torch.cuda.is_available():
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
else:
    pipe = StableDiffusionPipeline.from_pretrained(model_id)

pipe.save_pretrained("model")
