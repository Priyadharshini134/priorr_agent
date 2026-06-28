from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(result):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Automated Prior Authorization Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Patient Record</b>", styles["Heading2"]))
    elements.append(
        Paragraph(result["patient_record_text"].replace("\n", "<br/>"), styles["BodyText"])
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Clinical Summary</b>", styles["Heading2"]))
    elements.append(
        Paragraph(result["clinical_summary"].replace("\n", "<br/>"), styles["BodyText"])
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Policy Evaluation</b>", styles["Heading2"]))

    elements.append(
        Paragraph(
            f"<b>Policy:</b> {result['policy']['policy_name']}<br/>"
            f"<b>Description:</b> {result['policy']['description']}<br/>"
            f"<b>Status:</b> {result['rule_results']['overall_status']}",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Insurance Decision</b>", styles["Heading2"]))
    elements.append(
        Paragraph(
            f"<b>Company:</b> {result['insurance_decision']['Insurance Company']}<br/>"
            f"<b>Decision:</b> {result['insurance_decision']['Decision']}<br/>"
            f"<b>Date:</b> {result['insurance_decision']['Decision Date']}<br/><br/>"
            f"{result['insurance_decision']['Reason'].replace(chr(10), '<br/>')}",
            styles["BodyText"],
        )
    )

    doc.build(elements)