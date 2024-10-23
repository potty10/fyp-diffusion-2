# import torch
# from torch import autocast
# from diffusers import StableDiffusionPipeline

# model_id = "CompVis/stable-diffusion-v1-1"
# device = "cuda"


# pipe = StableDiffusionPipeline.from_pretrained(model_id)
# pipe = pipe.to(device)

# prompt = "a photo of an astronaut riding a horse on mars"
# with autocast("cuda"):
#     image = pipe(prompt)["sample"][0]  
    
# image.save("astronaut_rides_horse.png")



from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")
pipeline("An image of a squirrel in Picasso style").images[0].save("astronaut_rides_horse.png")


# # make sure you're logged in with `huggingface-cli login`
# from torch import autocast
# from diffusers import StableDiffusionPipeline

# pipe = StableDiffusionPipeline.from_pretrained(
# 	"CompVis/stable-diffusion-v1-4", 
# 	use_auth_token=True
# ).to("cuda")

# prompt = "a photo of an astronaut riding a horse on mars"
# with autocast("cuda"):
#     image = pipe(prompt)["sample"][0]  
    
# image.save("astronaut_rides_horse.png")