import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from state_schema import State

def generate_report(state: State) -> State:
    # JSON output
    json_report = json.dumps({
        "clauses": state.clauses,
        "overall_risk": state.overall_risk
    }, indent=2)
    # PDF output
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750
    c.drawString(30, y, "Contract Risk Analysis Report")
    y -= 30
    for clause, data in state.clauses.items():
        c.drawString(30, y, f"{clause}:")
        y -= 20
        c.drawString(50, y, f"Text: {data['text'][:80]}...")
        y -= 20
        c.drawString(50, y, f"Risk: {data['risk']}")
        y -= 20
        c.drawString(50, y, f"Comments: {data['comments']}")
        y -= 30
        if y < 100:
            c.showPage()
            y = 750
    c.drawString(30, y, f"Overall Risk: {state.overall_risk}")
    c.save()
    pdf_buffer.seek(0)
    return State(
        text=state.text,
        metadata=state.metadata,
        clauses=state.clauses,
        overall_risk=state.overall_risk,
        json_report=json_report,
        pdf_report=pdf_buffer
    ) 