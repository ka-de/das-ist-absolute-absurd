%cd /ComfyUI

model_downloads = [
    ###
    # LoRAs but unsorted on purpose hahaha
    "wget -O ./models/loras/tailgrab-xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Tailgrab.safetensors?download=true",

    ###
    # VAEs
    #"wget -O ./models/vae/xlVAEC_c1.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_c1.safetensors?download=true",
    #"wget -O ./models/vae/xlVAEC_c9.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_c9.safetensors?download=true",
    #"wget -O ./models/vae/xlVAEC_e7.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_e7.safetensors?download=true",
    #"wget -O ./models/vae/xlVAEC_f1.safetensors https://huggingface.co/k4d3/vae/resolve/main/xlVAEC_f1.safetensors?download=true",

    ###
    # AnimateDiff SDXL
    #"wget -O ./custom_nodes/ComfyUI-AnimateDiff-Evolved/models/mm_sdxl_v10_beta.ckpt https://huggingface.co/guoyww/animatediff/resolve/main/mm_sdxl_v10_beta.ckpt?download=true",

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
    # Bastard Lord
    # close-up portrait. Intricately detailed, the portrait will capture his piercing blue eyes, symbolizing wisdom and insight. His long beard, flowing down to his chest, represents age and experience. His furrowed brow signifies deep thought and contemplation. Hugin and Munin, perched upon his shoulders, high quality photography, 3 point lighting, flash with softbox, 4k, Canon EOS R3, hdr, smooth, sharp focus, high resolution, award winning photo, 80mm, f2.8, bokeh
    # https://tensor.art/models/681774055046654243
    #"wget -O ./models/checkpoints/bastard_xl.safetensors https://huggingface.co/k4d3/models2/resolve/main/bastard.safetensors?download=true",

    ###
    # Pony Diffusion V6
    # score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_furry, beautiful female anthro shark portrait, dramatic lighting, dark background
    # https://civitai.com/models/257749/pony-diffusion-v6-xl
    "wget -O ./models/checkpoints/ponyxl.safetensors https://huggingface.co/k4d3/models2/resolve/main/ponyxl.safetensors?download=true",
    #"wget -O ./models/checkpoints/ponyxl_turbo.safetensors https://huggingface.co/k4d3/models2/resolve/main/ponyxl_turbo.safetensors?download=true",
    #"wget -O ./models/checkpoints/ponyxl_turbo_dpo.safetensors https://huggingface.co/k4d3/models2/resolve/main/ponyxl_dpo_turbo.safetensors?download=true",

    ###
    # dreamshaperXL
    # In Casey Baugh's evocative style, art of a beautiful young girl cyborg with long brown hair, futuristic, scifi, intricate, elegant, highly detailed, majestic, Baugh's brushwork infuses the painting with a unique combination of realism and abstraction, greg rutkowski, surreal gold filigree, broken glass, (masterpiece, sidelighting, finely detailed beautiful eyes: 1.2), hdr, realistic painting, natural skin, textured skin, closed mouth, crystal eyes, butterfly filigree, chest armor, eye makeup, robot joints, long hair moved by the wind, window facing to another world, Baugh's distinctive style captures the essence of the girl's enigmatic nature, inviting viewers to explore the depths of her soul, award winning art
    # ugly, deformed, noisy, blurry, low contrast, text, BadDream, 3d, cgi, render, fake, anime, open mouth, big forehead, long neck
    # https://civitai.com/models/112902/dreamshaper-xl
    #"wget -O ./models/checkpoints/dreamshaper_turbo_dpmppsde_xl.safetensors https://huggingface.co/k4d3/models/resolve/main/dreamshaperXL_turboDpmppSDE.safetensors?download=true",


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
    # ??? *angery awoo*
    #
    #
    #"wget -O ./models/loras/pixel_art_style.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/pixel-art-xl-v1.1.safetensors?download=true",

    # The extraterrestrials have arrived!
    #"wget -O ./models/loras/kemosuit-PD-SDXL.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/kemosuit-PD-SDXL.safetensors?download=true",

    # Blacklight Slime Style [SDXL]
    # ral-blacklight
    # https://civitai.com/models/262835?modelVersionId=296343
    "wget -O ./models/loras/ral-blacklight-sdxl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/ral-blacklight-sdxl.safetensors?download=true",
    # Illustration style
    # ch
    # https://civitai.com/models/159778/illustration-style
    #"wget -O ./models/loras/chahua_illustration_style.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/chahua.safetensors?download=true",
    #
    # SDXL Anime style Lora
    # https://civitai.com/models/122660/sdxl-anime-style-lora
    #"wget -O ./models/loras/sdxl_anime_style.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/last-000014.safetensors?download=true",
    # T-shirt designs, Vector style, Stckers, POD
    # t-shirt design, sticker
    # https://civitai.com/models/125267/t-shirt-designs-vector-style-stckers-pod
    #"wget -O ./models/loras/tshirt_vector_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/last.safetensors?download=true",
    # OilPaint SDXL
    # style by nty
    # https://civitai.com/models/137963/oilpaint-sdxl
    #"wget -O ./models/loras/oilpaint_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/model_SDXL.safetensors?download=true",

    ## TODO: BAD LINKS!
    # Moebius (Jean Giraud) Style
    # Moebius \(Jean Giraud\) Style page
    # https://civitai.com/models/74776/moebius-jean-giraud-style
    #"wget -O ./models/loras/jean_giraud_style.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Moebius%20(Jean%20Giraud)%20Style.safetensors?download=true",
    # "LucasArts Style" (1990s PC Adventure Games) - SDXL LoRA - (Dreambooth Trained)
    # lcas artstyle
    # https://civitai.com/models/151539/lucasarts-style-1990s-pc-adventure-games-sdxl-lora-dreambooth-trained
    #"wget -O ./models/loras/lucasarts_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Lucasarts%20Artstyle%20-%20(Trigger%20is%20lcas%20artstyle).safetensors?download=true",

    ###
    # Enhancers and Fixers
    # (masterpiece,best quality,ultra_detailed,highres,absurdres:1.2)
    # (worst quality, low quality, ugly:1.4), poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, blurry, (bad art, bad anatomy:1.4), blurred, text, watermark,
    # https://civitai.com/models/116480/sdxl10neg4allxlboth-positive-high-qualitydetails-and-negative-worse-qualitybad-hand-in-one-lora
    "wget -O ./models/loras/neg4all_bdsqlsz_xl_V7.safetensors https://huggingface.co/k4d3/loras-xl/resolve/5ecd578976265b4e700376d8b4424f599de7abbd/neg4all_bdsqlsz_xl_V7.safetensors?download=true",
    # EasyFix [Negative LoRA] SDXL
    # overfit style (in the negative)
    # https://civitai.com/models/149316/easyfix-negative-lora-sdxl
    "wget -O ./models/loras/easyfix_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/EasyFix.safetensors?download=true",
    # Advanced Enhancer XL LoRA
    # movie still, film still, cinematic, cinematic shot, cinematic lighting, macro shot, 35mm film, green eyes, blue eyes, brown eyes, close up, teeth, braces
    # https://civitai.com/models/124993/advanced-enhancer-xl-lora
    "wget -O ./models/loras/advanced_enhancer_v2_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/AdvancedEnhancerXLv2.safetensors?download=true",
    # Perfect Eyes XL
    # green eyes, blue eyes, brown eyes, perfecteyes
    # https://civitai.com/models/118427/perfect-eyes-xl
    "wget -O ./models/loras/perfecteyes_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/PerfectEyesXL.safetensors?download=true",
    #
    #
    #
    "wget -O ./models/loras/badhands_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/badhands.safetensors?download=true",
    #
    #
    #
    "wget -O ./models/loras/xdetail_light_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/XDetail_light.safetensors?download=true",
    #
    #
    #
    "wget -O ./models/loras/add_detail_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/add-detail-xl.safetensors?download=true",
    # Concept: Perfect Eyes
    # perfecteyes
    # https://civitai.com/models/119399/concept-perfect-eyes
    "wget -O ./models/loras/perfect_eyes_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/lora-sdxl-perfect-eyes.safetensors?download=true",
    #
    #
    #
    "wget -O ./models/loras/more_art_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/xl_more_art-full_v1.safetensors?download=true",

    ###
    # Style Loras

    # John Harris Style
    # John Harris Style page
    # https://civitai.com/models/101986/john-harris-style
    #"wget -O ./models/loras/john_harris_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/John%20Harris%20Style.safetensors?download=true",
    # John Kenn Mortensen Style
    # John Kenn Mortensen Style page
    # https://civitai.com/models/101991/john-kenn-mortensen-style
    #"wget -O ./models/loras/john_kenn_mortensen_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/John%20Kenn%20Mortensen%20Style.safetensors?download=true",
    # John Martin Style
    # John Martin Style page
    # https://civitai.com/models/102786/john-martin-style
    #"wget -O ./models/loras/john_martin_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/John%20Martin%20Style.safetensors?download=true",
    # PixelArtRedmond - Pixel Art Loras for SD XL
    # Pixel Art, PixArFK
    # https://civitai.com/models/144684/pixelartredmond-pixel-art-loras-for-sd-xl
    #"wget -O ./models/loras/pixelart_redmond_lite64_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/PixelArtRedmond-Lite64.safetensors?download=true",
    # Flat illustration, office business
    # uran_style
    # https://civitai.com/models/147923/flat-illustration-office-business
    #"wget -O ./models/loras/flat_style_2_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/flat.safetensors?download=true",

    # Ghibli Style
    # ghibli
    # https://civitai.com/models/120860/sdxl10-ghibli-style-v1
    #"wget -O ./models/loras/ghibli_style_2_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/ghibli_last.safetensors?download=true",
    # Greg Rutkowski Inspired Style
    # Greg Rutkowski
    # https://civitai.com/models/117635/greg-rutkowski-inspired-style-lora-sdxl
    #"wget -O ./models/loras/greg_rutkowski_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/greg_rutkowski_xl_2.safetensors?download=true",
    # Greg Rutkowski
    # greg rutkowski
    # https://civitai.com/models/187011/greg-rutkowski-art-syle-capture-lora-xl
    #"wget -O ./models/loras/greg_rutkowski_style_2_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/greg_rutkowski_xl_v3.safetensors?download=true",
    # Guild Wars [Art Style Capture] Fantasy
    # guild wars
    # https://civitai.com/models/132940/guild-wars-art-style-capture-fantasy-lora-xl
    #"wget -O ./models/loras/guild_wars_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/guild_wars_xl_v5.safetensors?download=true",
    # Hisiya Anime
    #
    # https://civitai.com/models/188429/hisiya-anime-art-style-capture-lora-xl
    #"wget -O ./models/loras/hisiya_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/hisiya_xl_v1.safetensors?download=true",
    # Comic style - Jhyd
    # jhyd style
    # https://civitai.com/models/134144/comic-style-sdxl-jhyd-sdxl
    #"wget -O ./models/loras/jhyd_comic_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/jhyd-comic-style.safetensors?download=true",
    # Mandalorian
    # mndlr, mndlr style
    # https://civitai.com/models/119304/style-mandalorian
    #"wget -O ./models/loras/mandalorian_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/mndlr-000032.safetensors?download=true",
    # Nendoroid
    # nendoroid, chibi
    # https://civitai.com/models/126430/hevok-nendoroid-chibi-art-style-capture-lora-xl
    #"wget -O ./models/loras/nendoroid_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/nendoroid_xl_v8.safetensors?download=true",
    # SDXL Anime - Ecchi - Lewd - NSFW - Nuclear LoCon
    # nsfwnkean
    # https://civitai.com/models/144424/sdxl-anime-ecchi-lewd-nsfw-nuclear-locon
    #"wget -O ./models/loras/nsfwnkean_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/nsfwnkean8.safetensors?download=true",
    # Dissolve
    # ral-dissolve
    # https://civitai.com/models/245889/dissolve-style-sdxl
    #"wget -O ./models/loras/dissolve_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/ral-dissolve-sdxl.safetensors?download=true",
    # Retro Anime
    # retanime
    # https://civitai.com/models/237773/retro-anime
    #"wget -O ./models/loras/retro_anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/retanimev1.safetensors?download=true",
    # Style Squeeze
    #
    # https://civitai.com/models/214842/style-squeeze-xl-lora
    #"wget -O ./models/loras/stylesqueeze_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/stylesqueeze_v3_xl.safetensors?download=true",
    # Satoshi Urushihara style
    # urushisato, ova, background
    # https://civitai.com/models/7227/satoshi-urushihara-style
    #"wget -O ./models/loras/urushihara_satoshi_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/xl_urushihara_satoshi_v16.safetensors?download=true",
    # YAMER'S STYLE Princeps Omnia
    # yamer style
    # https://civitai.com/models/134810/sdxl-yamers-style-princeps-omnia-lora
    #"wget -O ./models/loras/yamer_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/xl_yamer_style-3.0.safetensors?download=true",
    # Style of Don Lawrence
    # st0rmstyl3, style of don lawrence, science fiction
    # https://civitai.com/models/123680/style-of-don-lawrence-sdxl
    #"wget -O ./models/loras/donlawrence_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/donlawrence-xl.safetensors?download=true",
    # Style of Jean-Pierre Gibrat
    # illustration by Jean-Pierre Gibrat
    # https://civitai.com/models/239745/style-of-jean-pierre-gibrat-xl
    #"wget -O ./models/loras/jean_pierre_gibrat_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/byJeanPierreGibratXL.safetensors?download=true",
    # LineAniRedmond- Linear Manga Style, Anime
    # lineart, LineAniAF
    # https://civitai.com/models/127018/lineaniredmond-linear-manga-style-for-sd-xl-anime-style
    #"wget -O ./models/loras/lineaniredmond_lineart_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/LineAniRedmondV2-Lineart-LineAniAF.safetensors?download=true",
    # DreamART Style
    #
    # https://civitai.com/models/105491/dreamart-style-lora
    #"wget -O ./models/loras/dreamart_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/DreamARTSDXL.safetensors?download=true",
    # Stylized Setting (Isometric)
    # Isometric_Setting
    # https://civitai.com/models/118775/stylized-setting-isometric-sdxl-and-sd15
    #"wget -O ./models/loras/stylized_isometric_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Stylized_Setting_SDXL.safetensors?download=true",
    # Voxel Style
    # voxel style
    # https://civitai.com/models/118536/voxel-xl
    #"wget -O ./models/loras/voxel_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/VoxelXL_v1.safetensors?download=true",
    # STYLIZARD - 3D Stylized Character Prototyping
    #
    # https://civitai.com/models/189726/stylizard-3d-stylized-character-prototyping
    #"wget -O ./models/loras/stylzard_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/STYLIZARD_v1.safetensors?download=true",
    # Analog
    # analog, AnalogRedmAF
    # https://civitai.com/models/129689/analogredmond-analog-style-photography-lora-for-sd-xl
    #"wget -O ./models/loras/analog_redmond_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/AnalogRedmondV2-Analog-AnalogRedmAF.safetensors?download=true",
    # ClassipeintXL (oil paint style LoRA)
    # oil painting
    # https://civitai.com/models/127139/classipeintxl-oil-paint-style-lora
    #"wget -O ./models/loras/classipeint_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/ClassipeintXL2.0.safetensors?download=true",
    # Dungeons & Dragons [Art Style Capture] Fantasy LoRA XL
    # dungeons and dragons
    # https://civitai.com/models/134343/dungeons-and-dragons-art-style-capture-fantasy-lora-xl
    #"wget -O ./models/loras/dungeons_and_dragons_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/dungeons_and_dragons_xl_v3.safetensors?download=true",
    # SDXL Film Photography Style
    # film photography style, light grain, medium grain, heavy grain
    # https://civitai.com/models/158945/sdxl-film-photography-style
    #"wget -O ./models/loras/film_photography_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors?download=true",
    # Cyberpunk Anime Style
    #
    # https://civitai.com/models/128568/cyberpunk-anime-style
    #"wget -O ./models/loras/cyberpunk_anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Cyberpunk%20_Anime_sdxl.safetensors?download=true",
    # Alphonse Mucha Style
    # Alphonse Mucha Style page
    # https://civitai.com/models/63072/alphonse-mucha-style
    #"wget -O ./models/loras/alphonse_mucha_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Alphonse%20Mucha%20Style.safetensors?download=true",
    # Frank Frazetta SDXL 1.0 art style lora
    # fr4z3tt4
    # https://civitai.com/models/119461/frank-frazetta-sdxl-10-art-style-lora
    #"wget -O ./models/loras/frazetta_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/fr4z3tt4.safetensors?download=true",
    # chinese style illustration
    # guofeng, chinese style
    # https://civitai.com/models/120206/sdxlchinese-style-illustration
    #"wget -O ./models/loras/chinese_illustration_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/chinese-style-illustration-guofeng.safetensors?download=true",
    # SDXL Paint Splash Style
    # Colorsplash
    # https://civitai.com/models/140335/sdxl-paint-splash-style
    #"wget -O ./models/loras/paintsplash_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/SDXLPaintSplash.safetensors?download=true",
    # Watercolor Style
    #
    # https://civitai.com/models/121538/watercolor-style-sdxl-and-15
    #"wget -O ./models/loras/watercolor_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/watercolor_v1_sdxl.safetensors?download=true",
    # PS1 Graphics SDXL
    # ps1 style
    # https://civitai.com/models/129556/ps1-graphics-sdxl
    #"wget -O ./models/loras/ps1_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/ps1_style_SDXL_v2.safetensors?download=true",
    # Dark Art Style
    #
    # https://civitai.com/models/161205/dark-art-style
    #"wget -O ./models/loras/nicola_samori_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/NicolaSamori.safetensors?download=true",
    # AnimeLoRA SDXL
    # anime
    # https://civitai.com/models/126750/animelora-sdxl
    #"wget -O ./models/loras/anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/anime_sdxl_v1.safetensors?download=true",
    # Futureistic Fantasy Anime SDXL
    # futuristic-fantasy-anime
    # https://civitai.com/models/123054/futureistic-fantasy-anime-sdxl
    #"wget -O ./models/loras/futuristic_fantasy_anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/futureistic_fantasy_anime_sdxl_v1.safetensors?download=true",
    # PE Anime Background / Landscapes [Style]
    # PEAnimeBG, Background, anime, scenery
    # https://civitai.com/models/137169/pe-anime-background-landscapes-style
    #"wget -O ./models/loras/pe_animebg_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/PE_AnimeBG.safetensors?download=true",
    # AnimeStyle Slider XL v1.1 -by AutoRunMech
    #
    # https://civitai.com/models/129020/animestyle-slider-xl-v11-by-autorunmech
    #"wget -O ./models/loras/anime_style_autorunmech_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/AnimeStyleXL_v1.1_AutoRunMech.safetensors?download=true",
    # Artist Coloring Style Lora - SDXL Anime Style
    #
    # https://civitai.com/models/123172/artist-coloring-style-lora-sdxl-anime-style
    #"wget -O ./models/loras/colorful_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/colorful_sdxl_v2_lbw.safetensors?download=true",
    # Flat Color Anime XL
    # flat color
    # https://civitai.com/models/180891/flat-color-anime-xl
    #"wget -O ./models/loras/flat_color_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/flatcolorxl.safetensors?download=true",
    # Envy Anime Oil XL 01
    # oil painting
    # https://civitai.com/models/160066/envy-anime-oil-xl-01
    #"wget -O ./models/loras/envy_anime_oil_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/EnvyAnimeOilXL01.safetensors?download=true",
    # cute anime XL
    # anime
    # https://civitai.com/models/124850/cute-anime-xl
    #"wget -O ./models/loras/cute_anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/cute-anime%20v1.safetensors?download=true",
    # BeksinskiXL
    # digital artwork by Beksinski
    # https://civitai.com/models/184519/beksinskixl
    #"wget -O ./models/loras/beksinski_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/sdxl_lora_beksinski-000018.safetensors?download=true",
    # painterly-XL
    # digital art, vivid fantasy colors
    # https://civitai.com/models/105689/painterly-xl
    #"wget -O ./models/loras/painterly_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/painterly-XL-v2.safetensors?download=true",
    # RetouchXL
    # 3D render, digital, game art
    # https://civitai.com/models/189022/retouchxl
    #"wget -O ./models/loras/retouchxl_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/RetouchXL_v2.3.safetensors?download=true",
    # Mythoscape Visions
    # Digital Art Style of a
    # https://civitai.com/models/214456/mythoscape-visions
    #"wget -O ./models/loras/mythoscape_digitalart_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Mythoscape%20Visions%20-%20Digital%20Art%20Style%20of%20a.safetensors?download=true",
    # LaxpeintXL (digital paint style LoRA)
    # digital painting
    # https://civitai.com/models/138424/laxpeintxl-digital-paint-style-lora
    #"wget -O ./models/loras/laxpeint_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/LaxpeintXL-2.0.safetensors?download=true",
    # Envy Digital Painting XL 01
    # digital painting
    # https://civitai.com/models/201819/envy-digital-painting-xl-01
    #"wget -O ./models/loras/envy_digitalpainting_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/EnvyDigitalPaintingXL01.safetensors?download=true",
    # Digital Artist style (Andreas Rocha)
    # Painted By Andreas Rocha
    # https://civitai.com/models/185470/digital-artist-style-andreas-rocha
    #"wget -O ./models/loras/andreas_rocha_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/DigitalArtist_Andreas_Rocha.safetensors?download=true",
    # Digital art hero style | SDXL
    #
    # https://civitai.com/models/216661/digital-art-hero-style-or-sdxl
    #"wget -O ./models/loras/herocool_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/herocoolstyle.safetensors?download=true",
    # 1990s ShoujoManga Anime Style [XLlora]
    #
    # https://civitai.com/models/130045/1990s-shoujomanga-anime-style-xllora
    #"wget -O ./models/loras/90s_shojou_manga_anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/1990s%20ShoujoManga%20Anime%20Style%20%5BXLlora%5D.safetensors?download=true",
    # HandDrawnAnime XL
    # 2d anime hand-drawn digital sketch style
    # https://civitai.com/models/153174/handdrawnanime-xl
    #"wget -O ./models/loras/handdrawn_anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/HandDrawnAnimeV1.safetensors?download=true",
    # CatCat-XL An anime style model for SDXL
    # anime style, cat ears, cute, masterpiece, best quality
    # https://civitai.com/models/119681/catcat-xl-an-anime-style-model-for-sdxl
    #"wget -O ./models/loras/catcat_anime_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/catcat-xl.safetensors?download=true",
    # Fusion Graphic
    # graphical anime
    # https://civitai.com/models/183386/fusion-graphic
    #"wget -O ./models/loras/fusion_graphic_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Fusion_Graphic_SDXL.safetensors?download=true",
    # SDXL Lora Anime / BlackClover
    # bc style
    # https://civitai.com/models/119416/sdxl-lora-anime-blackclover
    #"wget -O ./models/loras/anime_blackclover_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/anime-blackclover.safetensors?download=true",
    # Jasmine Art Style SDXL 1.0
    # jsmn style
    # https://civitai.com/models/118845/jasmine-art-style-sdxl-10
    #"wget -O ./models/loras/jasmine_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/JasmineStyleV2.safetensors?download=true",
    # John Berkey Style
    # John Berkey Style page
    # https://civitai.com/models/71182/john-berkey-style
    #"wget -O ./models/loras/john_berkey_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/John%20Berkey%20Style.safetensors?download=true",
    # H. R. Giger SDXL 1.0 art style lora
    # g1g3r
    # https://civitai.com/models/122752/h-r-giger-sdxl-10-art-style-lora
    #"wget -O ./models/loras/giger_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/g1g3r.safetensors?download=true",
    # Cute&Healthy Anime Girls - little as109 style
    # 1girl, as109, teen girls,
    # https://civitai.com/models/130369/cuteandhealthy-anime-girls-little-as109-style
    #"wget -O ./models/loras/teengirls_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/teengirls_reg.safetensors?download=true",
    # Pencil Art B&W (Jasmine style) XL 1.0
    # jsbw style
    # https://civitai.com/models/119771/pencil-art-bandw-jasmine-style-xl-10
    #"wget -O ./models/loras/jasmine_bwxldogumini_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/JasmineBWXLDoguMini.safetensors?download=true",
    # Arcane Style LoRA XL
    # arcane
    # https://civitai.com/models/112904/arcane-style-lora-xl
    #"wget -O ./models/loras/arcane_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/arcane_xl.safetensors?download=true",
    # Simon Stålenhag Style
    # Simon Stålenhag Style
    # https://civitai.com/models/51230/simon-stalenhag-style
    #"wget -O ./models/loras/simon_stalenhag_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Simon%20Stalenhag.safetensors?download=true",
    # Gustave Doré Style
    # Gustave Doré Style page
    # https://civitai.com/models/68346/gustave-dore-style
    #"wget -O ./models/loras/gustav_dore_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Gustave%20Dore%20Style.safetensors?download=true",
    # Art Frahm 1950s pin-up style XL
    # 1950s
    # https://civitai.com/models/180569/art-frahm-1950s-pin-up-style-xl
    #"wget -O ./models/loras/art_frahm_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Art_Frahm.safetensors?download=true",
    # Steampunk [Style] LoRA XL
    #
    # https://civitai.com/models/135168/steampunk-style-lora-xl
    #"wget -O ./models/loras/steampunk_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/steampunk_xl_v2.safetensors?download=true",
    # Studio Ghibli Style
    # Studio Ghibli Style
    # https://civitai.com/models/106712/studio-ghibli-style
    #"wget -O ./models/loras/ghibli_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Studio%20Ghibli%20Style.safetensors?download=true",
    # Fantasy Art XL
    # Art by Boris Vallejo, Boris Vallejo Art Style
    # https://civitai.com/models/122806/fantasy-art-xl
    #"wget -O ./models/loras/fantasy_art_v1_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Fantasy_art_XL_V1.safetensors?download=true",
    # SDXL Stencil Style
    # stencil style, stenciled
    # https://civitai.com/models/146293/sdxl-stencil-style
    #"wget -O ./models/loras/stencil_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/SDXLStencilStyleFAE.safetensors?download=true",
    # Liam Wong Style
    # Liam Wong Style page
    # https://civitai.com/models/73318/liam-wong-style
    #"wget -O ./models/loras/liam_wong_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Liam%20Wong%20Style.safetensors?download=true",
    # Flat style
    # Flat style
    # https://civitai.com/models/188798/flat-style
    #"wget -O ./models/loras/flat_style_xl.safetensors https://huggingface.co/k4d3/loras-xl/resolve/main/Flat%20style-000014.safetensors?download=true",
]

# Use ThreadPoolExecutor for parallel execution
with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel_tasks) as executor:
    #executor.map(run_command, model_downloads)
    results = list(executor.map(run_command, model_downloads))

# Print the results
for result in results:
    print(result)