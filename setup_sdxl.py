%cd /ComfyUI

model_downloads = [

    ###
    # VAEs
    #"wget -O ./models/vae/xlVAEC_c1.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_c1.safetensors?download=true",
    #"wget -O ./models/vae/xlVAEC_c9.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_c9.safetensors?download=true",
    #"wget -O ./models/vae/xlVAEC_e7.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_e7.safetensors?download=true",
    #"wget -O ./models/vae/xlVAEC_f1.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_f1.safetensors?download=true",

    ###
    # Frame interpolation
    #"wget -O ./custom_nodes/ComfyUI-Frame-Interpolation/ckpts/film/film_net_fp32.pt https://huggingface.co/k4d3/motion_models/resolve/main/film_net_fp32.pt?download=true",

    ###
    # Checkpoints SDXL
    #"wget -O ./models/checkpoints/asgardSDXLHybrid_v12FP16.safetensors https://huggingface.co/k4d3/models2/resolve/main/asgardSDXLHybrid_v12FP16.safetensors?download=true",

    ###
    # Yamer's PixelDiffusion
    # pixel art, digital oil pastel on canvas, animal, furry, upper body of a cyberpunk raven dressed in black techwear jacket, eye visor
    # bad quality, bad anatomy, worst quality, low quality, low resolution, extra fingers, blur, blurry, ugly, wrong proportions, watermark, image artifacts, lowres, ugly,  jpeg artifacts, deformed, noisy image, deformation, skin moles
    # https://civitai.com/models/277680?modelVersionId=312883
    #"wget -O ./models/checkpoints/pixelDiffusion_xl.safetensors https://huggingface.co/k4d3/models2/resolve/main/pixelDiffusion_pixelWorld.safetensors?download=true",

    ###
    # Asgard
    #"wget -O ./models/checkpoints/asgardSDXLHybrid_v12FP16.safetensors https://huggingface.co/k4d3/models2/resolve/main/asgardSDXLHybrid_v12FP16.safetensors?download=true",

    ###
    # Pony Diffusion V6
    # score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_furry, beautiful female anthro shark portrait, dramatic lighting, dark background
    # https://civitai.com/models/257749/pony-diffusion-v6-xl
    "wget -O ./models/checkpoints/ponyxl.safetensors https://huggingface.co/k4d3/models2/resolve/main/ponyxl.safetensors?download=true",
    #"wget -O ./models/checkpoints/ponyxl_turbo.safetensors https://huggingface.co/k4d3/models2/resolve/main/ponyxl_turbo.safetensors?download=true",
    #"wget -O ./models/checkpoints/ponyxl_turbo_dpo.safetensors https://huggingface.co/k4d3/models2/resolve/main/ponyxl_dpo_turbo.safetensors?download=true",

    ###
    # LoRAs - SDXL

    ###
    # LCM
    #"wget -O ./models/loras/lcm_sdxl.safetensors https://huggingface.co/latent-consistency/lcm-lora-sdxl/resolve/main/pytorch_lora_weights.safetensors?download=true",

    ###
    # Pixel Art
    #"wget -O ./models/loras/pxx4_v1_alpha.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/pxx4_v1_alpha.safetensors?download=true",
    #"wget -O ./models/loras/pixel-art-xl-v1.1.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/pixel-art-xl-v1.1.safetensors?download=true",

    ###
    # My LoRAs
    # ----
    # Blue Frost
    # https://civitai.com/models/229938/blue-frost
    #"wget -O ./models/loras/blue_frost_xl.safetensors https://huggingface.co/k4d3/myloras/resolve/main/blue_frost.safetensors?download=true",

    ###
    # Character LoRAs

    "wget -O ./models/loras/blaidd-v1e400.safetensors https://huggingface.co/k4d3/myloras/resolve/main/blaidd-v1e400.safetensors?download=true",
    "wget -O ./models/loras/foxparks-v2e134.safetensors https://huggingface.co/k4d3/myloras/resolve/main/foxparks-v2e134.safetensors?download=true",
    "wget -O ./models/loras/chillet-v3e10.safetensors https://huggingface.co/k4d3/myloras/resolve/main/chillet-v3e10.safetensors?download=true",
    "wget -O ./models/loras/lovander-v3e10.safetensors https://huggingface.co/k4d3/myloras/resolve/main/lovander-v3e10.safetensors?download=true",
    "wget -O ./models/loras/maliketh-v1e1.safetensors https://huggingface.co/k4d3/myloras/resolve/main/maliketh-v1e1.safetensors?download=true",

    ###
    # Style LoRAs

    "wget -O ./models/loras/wjs07-v1e200.safetensors https://huggingface.co/k4d3/myloras/resolve/main/wjs07-v1e200.safetensors?download=true",
    "wget -O ./models/loras/jinxit-v1e10.safetensors https://huggingface.co/k4d3/myloras/resolve/main/jinxit-v1e10.safetensors?download=true",
    "wget -O ./models/loras/louart-v1e10.safetensors https://huggingface.co/k4d3/myloras/resolve/main/louart-v1e10.safetensors?download=true",
    "wget -O ./models/loras/squishy-v1e10.safetensors https://huggingface.co/k4d3/myloras/resolve/main/squishy-v1e10.safetensors?download=true",
    "wget -O ./models/loras/goronic-v1e1.safetensors https://huggingface.co/k4d3/myloras/resolve/main/goronic-v1e1.safetensors?download=true",
    "wget -O ./models/loras/cecily_lin-v1e37.safetensors https://huggingface.co/k4d3/myloras/resolve/main/cecily_lin-v1e37.safetensors?download=true",
    "wget -O ./models/loras/cooliehigh-v1e45.safetensors https://huggingface.co/k4d3/myloras/resolve/main/cooliehigh-v1e45.safetensors?download=true",
    "wget -O ./models/loras/whisperingfornothing-v1e58.safetensors https://huggingface.co/k4d3/myloras/resolve/main/whisperingfornothing-v1e58.safetensors?download=true",
    "wget -O ./models/loras/kame_3-v1e80.safetensors https://huggingface.co/k4d3/myloras/resolve/main/kame_3-v1e80.safetensors?download=true",
    "wget -O ./models/loras/skecchiart-v1e134.safetensors https://huggingface.co/k4d3/myloras/resolve/main/skecchiart-v1e134.safetensors?download=true",
    "wget -O ./models/loras/darkgem_ponyxl_v1e4.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/darkgem_ponyxl_v1e4.safetensors?download=true",
    "wget -O ./models/loras/kenket_ponyxl_v1e4.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/kenket_ponyxl_v1e4.safetensors?download=true",
    "wget -O ./models/loras/chunie_ponyxl_v1e5.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/chunie_ponyxl_v1e5.safetensors?download=true",
    "wget -O ./models/loras/honovy_ponyxl_v1e4.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/honovy_ponyxl_v1e4.safetensors?download=true",
    "wget -O ./models/loras/woolrool_ponyxl_v1e4.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/woolrool_ponyxl_v1e4.safetensors?download=true",

    ###
    # Concept loras
    "wget -O ./models/loras/tailgrab-xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Tailgrab.safetensors?download=true",

    ###
    # Enhancers and fixes
    "wget -O ./models/loras/neg4all_bdsqlsz_xl_V7.safetensors https://huggingface.co/k4d3/loras-xl/resolve/5ecd578976265b4e700376d8b4424f599de7abbd/neg4all_bdsqlsz_xl_V7.safetensors?download=true",
    "wget -O ./models/loras/easyfix_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/EasyFix.safetensors?download=true",
    "wget -O ./models/loras/advanced_enhancer_v2_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/AdvancedEnhancerXLv2.safetensors?download=true",
    "wget -O ./models/loras/perfecteyes_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/PerfectEyesXL.safetensors?download=true",
    "wget -O ./models/loras/badhands_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/badhands.safetensors?download=true",
    "wget -O ./models/loras/xdetail_light_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/XDetail_light.safetensors?download=true",
    "wget -O ./models/loras/add_detail_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/add-detail-xl.safetensors?download=true",
    "wget -O ./models/loras/perfect_eyes_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/lora-sdxl-perfect-eyes.safetensors?download=true",
    "wget -O ./models/loras/more_art_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/xl_more_art-full_v1.safetensors?download=true",
]

# Use ThreadPoolExecutor for parallel execution
with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel_tasks) as executor:
    #executor.map(run_command, model_downloads)
    results = list(executor.map(run_command, model_downloads))

# Print the results
for result in results:
    print(result)