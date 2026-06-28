def form_agent(state):

    patient = state["patient_data"]["patient"]

    form = {

        "Patient Name": patient["patient_name"],

        "Age": patient["age"],

        "Gender": patient["gender"],

        "Insurance Company": "MediClaim Health Insurance",

        "Provider": patient["provider_name"],

        "Diagnosis": patient["diagnosis"],

        "Treatment Requested": patient["medication"],

        "Policy": state["policy"]["policy_name"],

        "Clinical Summary": state["clinical_summary"],

        "Medical Necessity": state["policy_decision"],

        "Required Documents": [
            "Doctor Prescription",
            "Clinical Notes",
            "Lab Report"
        ]
    }

    return {
        "authorization_form": form
    }