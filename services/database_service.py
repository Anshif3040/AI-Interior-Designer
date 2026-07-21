from database import save_prediction


def save_room_prediction(
    prediction,
    confidence,
    length,
    width,
    height,
    area,
    style,
    total_budget
):

    save_prediction(
        prediction,
        confidence,
        float(length),
        float(width),
        float(height),
        area,
        style,
        total_budget
    )