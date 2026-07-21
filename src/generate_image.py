from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

def generate_image(prompt):
    image = pipe(prompt).images[0]
    image.save("static/output.png")
    return "static/output.png"