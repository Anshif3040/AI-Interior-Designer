from src.pdf_generator import create_pdf


def generate_report(
    prediction,
    confidence,
    length,
    width,
    height,
    area,
    style,
    recommendation,
    furniture,
    total_budget,
    prompt
):

    create_pdf(
        prediction,
        confidence,
        length,
        width,
        height,
        area,
        style,
        recommendation,
        furniture,
        total_budget,
        prompt
    )