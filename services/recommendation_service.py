from src.recommendations import get_recommendation
from src.furniture import get_furniture


def build_room_recommendations(prediction, style):

    recommendation = None
    furniture = []
    total_budget = 0

    if prediction and style:
        recommendation = get_recommendation(prediction, style)

    if prediction:
        furniture = get_furniture(prediction)
        total_budget = sum(price for item, price in furniture)

    return recommendation, furniture, total_budget