import requests
import urllib.parse


def generate_image(prompt):

    prompt = urllib.parse.quote(prompt)

    image_url = f"https://image.pollinations.ai/prompt/{prompt}"

    return image_url