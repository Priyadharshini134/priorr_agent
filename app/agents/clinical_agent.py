from app.config import llm


def clinical_agent(state):

    prompt = f"""
    Analyze the patient record.

    Extract:
- Diagnosis
- Symptoms
- Previous medications documented in the clinical notes
- Treatments that clinically failed (only if explicitly mentioned)

Do NOT infer treatment failure from prior authorization history or insurance decisions.

    Patient Record:

    {state["patient_record_text"]}
    """

    response = llm.invoke(prompt)
    print("Clinical Agent Output:")
    print(response.content)

    return {
        "clinical_summary": response.content
    }