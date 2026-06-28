from app.services.policy_service import (
    get_policy,
    get_policy_rules
)

from app.services.rule_engine import evaluate_policy


def policy_agent(state):

    patient = state["patient_data"]["patient"]

    observations = state["patient_data"]["observations"].copy()

# Add patient fields required by policy rules
    observations["Age"] = patient["age"]

# If needed later, you can also add:
    observations["Diagnosis"] = patient["diagnosis"]
    observations["Medication"] = patient["medication"]


    history = state["patient_data"]["history"]

    insurance_company = "MediClaim Health Insurance"

    diagnosis = patient["diagnosis"]

    treatment = patient["medication"]

    policy = get_policy(
        insurance_company,
        diagnosis,
        treatment
    )

    if policy is None:

        return {

            "policy_decision":
                "No matching insurance policy found.",

            "rule_results": {},

            "policy": {}
        }

    rules = get_policy_rules(
        policy["policy_id"]
    )

    result = evaluate_policy(

        {

            "observations": observations

        },

        rules

    )

    return {

        "policy": policy,

        "rule_results": result,

        "policy_text": policy["description"],

        "policy_decision":
            result["overall_status"]

    }