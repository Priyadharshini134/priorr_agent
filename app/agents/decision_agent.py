from datetime import date
from app.config import llm


def decision_agent(state):

    rule_results = state["rule_results"]
    overall = rule_results["overall_status"]

    prompt = f"""
You are a healthcare prior authorization reviewer.

Patient Clinical Summary

{state["clinical_summary"]}

Insurance Policy

{state["policy_text"]}

Rule Evaluation

{rule_results["results"]}

Overall Eligibility

{overall}

Instructions:

1. Write a Medical Necessity paragraph describing why the requested treatment is clinically appropriate.

2. Do NOT mention Approved, Denied, Eligible, or Not Eligible in the Medical Necessity section.

3. Write a separate Policy Justification explaining whether the patient satisfies the insurance policy.

4. Do NOT interpret previous prior authorization history as treatment failure.

5. Base your explanation only on:
   - Clinical Summary
   - Current Policy Rules
   - Rule Evaluation

Return the response in this format:

Medical Necessity:
...

Policy Justification:
...
"""

    response = llm.invoke(prompt)

    if overall == "Eligible":
        decision = "Approved"

    elif overall == "Not Eligible":

        decision = "Denied"

    elif overall == "Pending":

        decision = "Pending"

    else:

        decision = "Review Required"

    return {

        "policy_decision": response.content,

        "insurance_decision": {

            "Insurance Company": "MediClaim Health Insurance",

            "Decision": decision,

            "Decision Date": str(date.today()),

            "Reason": response.content
        },

        "final_decision": decision
    }