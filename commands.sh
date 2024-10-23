python scripts/txt2img.py --prompt "a balloon going into a cave" --plms --ckpt "./models/stable-diffusion-v1/sd-v1-1.ckpt"

python scripts/img2img.py --prompt "A man running from a nuclear explosion" --ckpt "./models/stable-diffusion-v1/sd-v1-1-full-ema.ckpt" --init-img "./test/test2.jpg" --strength 0.8