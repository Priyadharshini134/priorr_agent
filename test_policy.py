from app.services.policy_service import get_policy
from app.services.policy_service import get_policy_rules

policy = get_policy(
    "MediClaim Health Insurance",
    "Rheumatoid Arthritis",
    "Humira"
)

print(policy)

rules = get_policy_rules(policy["policy_id"])

print(rules)