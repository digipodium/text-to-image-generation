from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import io
from PIL import Image


def generate(sentence):
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": "Bearer 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"}
    image_bytes = query({"inputs": sentence })
    image = Image.open(io.BytesIO(image_bytes))
    fname = make_filename(sentence) 
    path = 'static/generated/' + fname
    image.save(path)
    return path

def make_filename(sentence):
    words = sentence.strip().split()
    # remove special characters
    filename = "_".join(words)
    filename = ''.join(e for e in filename if e.isalnum())[:20]
    return filename+".jpg"
