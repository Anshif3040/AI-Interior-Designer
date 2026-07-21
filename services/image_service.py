from src.image_generator import generate_image


def generate_ai_design(prompt):

    if not prompt:
        return None

    return generate_image(prompt)