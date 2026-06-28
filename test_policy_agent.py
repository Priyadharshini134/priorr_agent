from ehr_db import get_patient

from app.agents.policy_agent import policy_agent


# Get patient from EHR
patient = get_patient(2)      # Mary Johnson


# Create state similar to LangGraph state
state = {

    "patient_data": patient

}


# Run the policy agent
result = policy_agent(state)


print("\n========== POLICY AGENT OUTPUT ==========\n")

print(result["policy_text"])

print("\n=========================================\n")