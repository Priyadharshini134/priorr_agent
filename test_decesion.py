from app.agents.decision_agent import decision_agent



state = {

    "patient_data": {
        "patient": {
            "patient_name": "Mary Johnson",
            "age": 45,
            "gender": "Female",
            "diagnosis": "Rheumatoid Arthritis",
            "medication": "Humira",
            "provider_name": "Dr. Emily Brown"
        }
    },

    "clinical_summary": """
Patient has severe Rheumatoid Arthritis with inadequate response to Methotrexate.
CRP level is elevated at 24 mg/L.
""",

    "rule_results": {

        "results": [

            {
                "rule": "Previous Medication",
                "expected": "Methotrexate",
                "actual": "Methotrexate",
                "status": "PASS"
            },

            {
                "rule": "CRP",
                "expected": "10",
                "actual": "24",
                "status": "PASS"
            }

        ],

        "overall_status": "Eligible"

    }

}

result = decision_agent(state)

print(result)