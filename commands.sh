CUDA_VISIBLE_DEVICES=0/1/2/3 python scripts/txt2img.py --prompt "a balloon going into a cave" --ckpt "./models/stable-diffusion-v1/sd-v1-1.ckpt" --n_iter 1 --n_samples 1

python scripts/img2img.py --prompt "A man running from a nuclear explosion" --ckpt "./models/stable-diffusion-v1/sd-v1-1-full-ema.ckpt" --init-img "./test/test2.jpg" --strength 0.8

CUDA_VISIBLE_DEVICES=0/1/2/3 python scripts/ddim_inverse.py --prompt "a balloon going into a cave" --ckpt "./models/stable-diffusion-v1/sd-v1-1.ckpt" --n_iter 1 --n_samples 1