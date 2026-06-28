from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.state import AgentState

from app.agents.clinical_agent import clinical_agent
from app.agents.policy_agent import policy_agent
from app.agents.decision_agent import decision_agent
from app.agents.form_agent import form_agent

builder = StateGraph(AgentState)

# Nodes
builder.add_node(
    "clinical_agent",
    clinical_agent
)

builder.add_node(
    "policy_agent",
    policy_agent
)

builder.add_node(
    "decision_agent",
    decision_agent
)

builder.add_node(
    "form_agent",
    form_agent
)

# Flow
builder.add_edge(
    START,
    "clinical_agent"
)

builder.add_edge(
    "clinical_agent",
    "policy_agent"
)

builder.add_edge(
    "policy_agent",
    "decision_agent"
)

builder.add_edge(
    "decision_agent",
    "form_agent"
)

builder.add_edge(
    "form_agent",
    END
)

graph = builder.compile()