
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.graph import graph
from app.ehr_db import get_patient
from app.pdf_generator import generate_pdf
from fastapi.responses import FileResponse
from fastapi import HTTPException
import os


app = FastAPI(title="Prior Authorization API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add health endpoint HERE (after app is created)
@app.get("/health")
def health():
    print("Health endpoint called")
    return {"status": "ok"}


@app.get("/download-report")
def download_report():

    pdf_path = "report.pdf"

    if not os.path.exists(pdf_path):
        raise HTTPException(
            status_code=404,
            detail="PDF report not found. Please generate authorization first."
        )

    return FileResponse(
        path=pdf_path,
        filename="Authorization_Report.pdf",
        media_type="application/pdf"
    )

@app.post("/prior-auth/{patient_id}")
def prior_authorization(patient_id: int):

    # -------------------------------
    # Fetch Patient from Mock EHR
    # -------------------------------
    patient_data = get_patient(patient_id)

    if patient_data is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found."
        )

    patient = patient_data["patient"]

    # -------------------------------
    # Convert EHR to readable text
    # (Clinical Agent still uses this)
    # -------------------------------

    notes = "\n".join(
        note["note_text"]
        for note in patient_data["notes"]
    )

    labs = "\n".join(
        f'{lab["test_name"]} : {lab["result"]}'
        for lab in patient_data["labs"]
    )

    history = "\n".join(
        f'{item["treatment_requested"]} - {item["status"]}'
        for item in patient_data["history"]
    )

    patient_record_text = f"""

Patient Name : {patient["patient_name"]}
Age          : {patient["age"]}
Gender       : {patient["gender"]}
Diagnosis    : {patient["diagnosis"]}
Medication   : {patient["medication"]}
Provider     : {patient["provider_name"]}

Clinical Notes

{notes}

Lab Reports

{labs}

Previous Prior Authorization

{history}

"""

    # -----------------------------------
    # Run LangGraph Workflow
    # -----------------------------------

    result = graph.invoke({

        "patient_id": patient_id,

        "patient_record_text": patient_record_text,

        "patient_data": patient_data

    })
    

    try:
        generate_pdf(result)
        print("PDF generated successfully.")
    except Exception as e:
        print("PDF Generation Error:", e)


    # -----------------------------------
    # Return Response
    # -----------------------------------

    return {

    "patient_record_text":
        patient_record_text,

    "clinical_summary":
        result["clinical_summary"],

    "authorization_form":
        result["authorization_form"],

    "policy_evaluation": {

        "policy_name":
            result["policy"]["policy_name"],

        "policy_description":
            result["policy"]["description"],

        "rule_results":
            result["rule_results"]
    },

    "insurance_decision":
        result["insurance_decision"]
}