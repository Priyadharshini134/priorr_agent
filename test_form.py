from app.agents.form_agent import form_agent

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

    "clinical_summary":
    "Patient has severe Rheumatoid Arthritis with inadequate response to Methotrexate.",

    "medical_necessity":
    "Patient has severe Rheumatoid Arthritis with inadequate response to Methotrexate. CRP is elevated at 24 mg/L. The patient satisfies the insurer's medical necessity criteria for Humira therapy.",

    "policy": {

        "insurance_company":"MediClaim Health Insurance",

        "policy_name":"Biologic Therapy Prior Authorization"

    },

    "rule_results":{

        "results":[

            {

                "rule":"Previous Medication",

                "expected":"Methotrexate",

                "actual":"Methotrexate",

                "status":"PASS"

            },

            {

                "rule":"CRP",

                "expected":"10",

                "actual":"24",

                "status":"PASS"

            }

        ]

    },

    "policy_decision":"Eligible",

    "final_decision":"Approved"

}

result = form_agent(state)

print(result)