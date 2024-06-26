from diffusers import StableDiffusionPipeline  # latest version transformers (clips)
from diffusers import DiffusionPipeline # slow version
import torch
import base64
import io
from PIL import Image

torch.cuda.empty_cache() #empty vram

class ImageGen:
    def __init__(self):
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.detailed_model_id = "stabilityai/stable-diffusion-xl-base-1.0"

    def generate(self, prompt="Didn't work sorry", guidance_scaleImg=7.5, stepsImg=50, negativeImg="", num_images=1):
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16, safety_checker=None, filter_enabled=False)
        self.pipe = self.pipe.to("cuda")
        self.pipe.enable_model_cpu_offload()
        images = self.pipe(prompt=prompt,
                guidance_scale=guidance_scaleImg,
                num_inference_steps=stepsImg,
                negative_prompt=negativeImg,
                num_images_per_prompt=num_images
            ).images[0]
           # Format the base64 string as a data URL for HTML
        return self.covertToimgageJpeg(images);

    def generateDetailed(self, prompt="Didn't work sorry", guidance_scaleImg=7.5, stepsImg=50, negativeImg="", num_images=1):
        self.pipe = DiffusionPipeline.from_pretrained(self.detailed_model_id, torch_dtype=torch.float16, variant="fp16", filter_enabled=False, safety_checker=None)
        self.pipe = self.pipe.to("cuda")
        self.pipe.enable_model_cpu_offload()
        images = self.pipe(prompt=prompt,
                guidance_scale=guidance_scaleImg,
                num_inference_steps=stepsImg,
                negative_prompt=negativeImg,
                num_images_per_prompt=num_images
            ).images[0]
           # Format the base64 string as a data URL for HTML
        return self.covertToimgageJpeg(images);


    def covertToimgageJpeg(self, image):
        image = image.convert('RGB')
                        # Convert the image to a byte array
        with io.BytesIO() as buffer:
            image.save(buffer, format="JPEG")
            image_byte_array = buffer.getvalue()

            # Convert the image to a byte array
            # image_byte_array = image.tobytes()

            # Encode the byte array to base64
        base64_encoded_image = base64.b64encode(image_byte_array)

            # Convert the base64 bytes to a string
        base64_encoded_image_string = base64_encoded_image.decode('utf-8')

            # Format the base64 string as a data URL for HTML
        data_url = f"data:image/jpeg;base64,{base64_encoded_image_string}"
        return data_url