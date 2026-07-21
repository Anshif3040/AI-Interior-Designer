from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from config import OUTPUT_FOLDER
import os


def create_pdf(
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

    # outputs folder ഇല്ലെങ്കിൽ create ചെയ്യും
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    pdf_path = os.path.join(OUTPUT_FOLDER, "interior_report.pdf")
    pdf = SimpleDocTemplate(pdf_path)
    
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("AI INTERIOR DESIGN REPORT", styles["Title"]))

    story.append(Paragraph(f"<b>Room Type:</b> {prediction}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Confidence:</b> {confidence:.2f}%", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Room Measurements</b>", styles["Heading2"]))
    story.append(Paragraph(f"Length : {length} m", styles["BodyText"]))
    story.append(Paragraph(f"Width : {width} m", styles["BodyText"]))
    story.append(Paragraph(f"Height : {height} m", styles["BodyText"]))
    story.append(Paragraph(f"Area : {area} m²", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Style:</b> {style}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Interior Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(f"Wall Color : {recommendation['wall']}", styles["BodyText"]))
    story.append(Paragraph(f"Floor : {recommendation['floor']}", styles["BodyText"]))
    story.append(Paragraph(f"Lighting : {recommendation['lighting']}", styles["BodyText"]))
    story.append(Paragraph(f"Furniture : {recommendation['furniture']}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Furniture Recommendation</b>", styles["Heading2"]))

    for item, price in furniture:
        story.append(Paragraph(f"{item} - ₹{price:,}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))
    story.append(Paragraph(f"<b>Total Budget : ₹{total_budget:,}</b>", styles["Heading2"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))
    story.append(Paragraph("<b>AI Prompt</b>", styles["Heading2"]))
    story.append(Paragraph(prompt, styles["BodyText"]))

    pdf.build(story)