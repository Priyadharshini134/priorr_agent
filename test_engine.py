from ehr_db import get_patient

from app.services.policy_service import (
    get_policy,
    get_policy_rules
)

from app.services.rule_engine import evaluate_policy


# Patient ID
patient_id = 2

ehr = get_patient(patient_id)

policy = get_policy(
    "MediClaim Health Insurance",
    ehr["patient"]["diagnosis"],
    ehr["patient"]["medication"]
)

rules = get_policy_rules(policy["policy_id"])

patient_data = {
    "observations": {
        "CRP": "24",
        "Previous Medication": "Methotrexate"
    }
}

result = evaluate_policy(
    patient_data,
    rules
)

print(result)