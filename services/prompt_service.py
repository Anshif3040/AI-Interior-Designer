def create_prompt(prediction, style, area, height):

    return f"""
    {style} {prediction},
    {area} square meter room,
    {height} meter ceiling height,
    modern furniture,
    elegant lighting,
    realistic interior design
    """