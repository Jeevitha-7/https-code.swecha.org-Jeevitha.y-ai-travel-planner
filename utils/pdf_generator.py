from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(destination, budget, days, travelers, itinerary):
    """
    Generate a travel itinerary PDF.
    """

    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/{destination.lower()}_trip.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph(f"AI Travel Plan - {destination}", styles["Title"]))

    content.append(Spacer(1, 12))

    # Trip Details
    content.append(Paragraph(f"<b>Destination:</b> {destination}", styles["BodyText"]))

    content.append(Paragraph(f"<b>Budget:</b> ₹{budget}", styles["BodyText"]))

    content.append(Paragraph(f"<b>Days:</b> {days}", styles["BodyText"]))

    content.append(Paragraph(f"<b>Travelers:</b> {travelers}", styles["BodyText"]))

    content.append(Spacer(1, 15))

    # Itinerary
    content.append(Paragraph("Generated Itinerary", styles["Heading2"]))

    content.append(Spacer(1, 10))

    itinerary = itinerary.replace("\n", "<br/>")

    content.append(Paragraph(itinerary, styles["BodyText"]))

    doc.build(content)

    return filename
