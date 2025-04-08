!pip install gradio

#Image Transformer

import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import gradio as gr

def apply_transformation(image, transformation):
    # Convert to PIL Image
    img = Image.fromarray(image)

    if transformation == "Grayscale":
        img = img.convert("L").convert("RGB")

    elif transformation == "Brighten":
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.5)

    elif transformation == "Contour":
        img = img.filter(ImageFilter.CONTOUR)

    elif transformation == "Blur":
        img = img.filter(ImageFilter.BLUR)

    elif transformation == "Edge Detection":
        img = img.filter(ImageFilter.FIND_EDGES)

    elif transformation == "Sharpen":
        img = img.filter(ImageFilter.SHARPEN)

    elif transformation == "Invert":
        img = Image.fromarray(255 - np.array(img))

    return np.array(img)

# Gradio UI
interface = gr.Interface(
    fn=apply_transformation,
    inputs=[
        gr.Image(type="numpy", label="Upload Image"),
        gr.Dropdown(
            ["Grayscale", "Brighten", "Contour", "Blur", "Edge Detection", "Sharpen", "Invert"],
            label="Choose Transformation"
        )
    ],
    outputs=gr.Image(label="Transformed Image"),
    title="🧙‍♂️ Image Transformer",
    description="Apply cool transformations to your images using OpenCV + PIL + Gradio."
)

interface.launch()
