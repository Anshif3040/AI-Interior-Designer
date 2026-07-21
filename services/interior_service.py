from services.recommendation_service import build_room_recommendations
from services.prompt_service import create_prompt
from services.image_service import generate_ai_design


def process_interior(prediction, style, area, height):

    recommendation, furniture, total_budget = build_room_recommendations(
        prediction,
        style
    )

    prompt = create_prompt(
        prediction,
        style,
        area,
        height
    )

    generated_image = generate_ai_design(prompt)

    return (
        recommendation,
        furniture,
        total_budget,
        prompt,
        generated_image
    )