from diffusers import StableDiffusionPipeline
import torch

class StableDiffusion:
    def __init__(self, model_id="model"):
        if torch.cuda.is_available():
            device = "cuda"
            self.pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
        else:
            device = "cpu"
            self.pipe = StableDiffusionPipeline.from_pretrained(model_id)

        self.pipe = self.pipe.to(device)

    def __call__(self, prompt):
        return self.pipe(prompt).images[0]  
