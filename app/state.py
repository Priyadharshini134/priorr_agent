from typing import TypedDict


class AgentState(TypedDict, total=False):

    # Input from API
    patient_id: int
    patient_record_text: str
    patient_data: dict

    # Clinical Agent
    clinical_summary: str

    # Policy Agent
    policy: dict
    policy_text: str
    rule_results: dict
    policy_decision: str

    # Decision Agent
    final_decision: str

    # Form Agent
    authorization_form: dict

    insurance_decision: dict

    # PDF Output
    packet_path: str