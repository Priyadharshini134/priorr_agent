# Automated Prior Authorization Agent with Patient Consent Management

## 📌 Overview
An AI-powered healthcare automation system that streamlines the prior authorization process by analyzing patient medical records, evaluating insurance policy rules, and generating authorization forms and decisions.

The system uses Agentic AI to reduce manual effort, improve processing efficiency, and support faster authorization workflows.

## ✨ Key Features
- **Clinical Data Analysis:** Extracts relevant patient information and summarizes clinical records.
- **Insurance Policy Analysis:** Retrieves and evaluates insurance policy requirements.
- **Rule-Based Evaluation:** Checks eligibility criteria using a policy rule engine.
- **Multi-Agent Workflow:** Coordinates AI agents using LangGraph.
- **Authorization Form Generation:** Generates structured authorization forms.
- **REST API:** Exposes endpoints through FastAPI for workflow execution.

## 🛠️ Tech Stack
- **Language:** Python
- **Backend:** FastAPI
- **AI Orchestration:** LangGraph
- **LLM:** Ollama / Groq, depending on configuration
- **Database:** PostgreSQL
- **Frontend:** React, Tailwind CSS
- **API Testing:** Swagger UI

## 🔄 Workflow
1. Retrieve patient records from the database.
2. Analyze clinical information using the clinical agent.
3. Retrieve the relevant insurance policy.
4. Evaluate eligibility using the policy rule engine.
5. Generate the authorization decision and form.
6. Return the results through the API.

## ⚙️ Getting Started

### Prerequisites
- Python
- PostgreSQL
- Required LLM provider and model
- Node.js and npm (for the frontend)

### Installation

```bash
git clone https://github.com/Priyadharshini134/priorr_agent.git
cd priorr_agent

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Configure your database and LLM credentials using environment variables or your application's configuration.

Start the FastAPI backend using the appropriate module path for your project:

```bash
uvicorn app.api:app --reload
```

Open Swagger UI:

`http://127.0.0.1:8000/docs`

## 🔌 API Endpoint

**Method:** `POST`

**Endpoint:** `/prior-auth/{patient_id}`

Use Swagger UI to provide a patient ID and test the prior authorization workflow.

## 🔮 Future Enhancements
- Digital patient consent management.
- Support for multiple insurance policies.
- Workflow tracking and notifications.
- Integration with real-world EHR systems.

## 👩‍💻 Author
**Priyadharshini M**

GitHub: [Priyadharshini134](https://github.com/Priyadharshini134)
