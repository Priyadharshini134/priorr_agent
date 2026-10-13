# Automated Prior Authorization Agent with Patient Consent Management

An AI-powered healthcare automation system designed to streamline the insurance prior authorization process by analyzing patient records, evaluating insurance policy requirements, and generating authorization decisions.

## 📌 Project Overview

Prior authorization is a process in which healthcare providers obtain approval from an insurance company before providing certain medical treatments or medications. Traditional prior authorization involves manual documentation, policy verification, and repeated communication, which can lead to delays and administrative overhead.

This project uses **Agentic AI, Large Language Models (LLMs), and rule-based evaluation** to automate key steps in the prior authorization workflow.

## 🎯 Objectives

- Automate the prior authorization workflow.
- Extract relevant clinical information from patient records.
- Analyze insurance policies and eligibility criteria.
- Evaluate policy rules using a rule engine.
- Generate structured authorization forms and decision summaries.
- Improve efficiency, consistency, and transparency in authorization processing.
- Support patient consent management as part of the authorization workflow.

## ✨ Key Features

- **Clinical Data Analysis:** Extracts relevant information such as diagnosis, previous treatments, medications, and laboratory results.
- **Insurance Policy Analysis:** Loads insurance policy information and identifies applicable requirements.
- **Rule-Based Eligibility Evaluation:** Checks predefined conditions such as previous medication failure and laboratory values.
- **Agentic AI Workflow:** Coordinates multiple AI agents using LangGraph.
- **Authorization Decision Support:** Combines policy evaluation results and clinical information to determine an authorization outcome.
- **Authorization Form Generation:** Produces a structured authorization form containing relevant patient and clinical details.
- **REST API:** Provides endpoints to trigger and test the prior authorization workflow.
- **Web Interface:** Provides a frontend for interacting with the system.

## 🏗️ System Architecture

The application follows a modular architecture consisting of a frontend, backend API, AI agents, policy evaluation services, and a database.

```text
                User / Healthcare Provider
                          |
                          v
                 React Web Interface
                          |
                          v
                    FastAPI Backend
                          |
                          v
                  LangGraph Workflow
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
    Clinical Agent   Policy Agent    Decision Agent
          |               |               |
          v               v               v
     Patient Data    Policy Loader    Rule Engine
          |               |               |
          +---------------+---------------+
                          |
                          v
                 Authorization Form
                          |
                          v
                   Final Decision
```

## 🔄 Workflow

1. **Patient Record Retrieval:** The system retrieves patient information from the PostgreSQL database.
2. **Clinical Analysis:** The clinical agent extracts relevant medical information and summarizes the patient's condition.
3. **Policy Retrieval:** The policy service loads the applicable insurance policy and its requirements.
4. **Rule Evaluation:** The rule engine checks the patient's clinical data against the configured policy rules.
5. **Decision Processing:** The decision agent uses the available clinical and policy evaluation results to prepare the authorization outcome.
6. **Form Generation:** The system generates a structured authorization form.
7. **API Response:** The backend returns the processed information and authorization results to the client.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| AI Workflow Orchestration | LangGraph |
| Large Language Models | Ollama / Groq, depending on configuration |
| Database | PostgreSQL |
| Database Connectivity | psycopg2 |
| Frontend | React |
| UI Styling | Tailwind CSS |
| API Testing | Swagger UI |
| Data Processing | Python |

## 📂 Project Structure

The following is the logical structure of the project. Refer to the repository for the exact files and folders.

```text
priorr_agent/
├── app/
│   ├── api.py
│   ├── graph.py
│   ├── agents.py
│   ├── ehr_db.py
│   ├── pdf_parser.py
│   ├── policy_loader.py
│   └── report_generator.py
├── policies/
├── reports/
├── frontend/
├── requirements.txt
├── .gitignore
└── README.md
```

- `api.py` – Defines the FastAPI endpoints.
- `graph.py` – Defines the LangGraph workflow and agent execution order.
- `agents.py` – Contains the AI agent logic.
- `ehr_db.py` – Handles patient data retrieval from PostgreSQL.
- `pdf_parser.py` – Supports extracting text from PDF documents.
- `policy_loader.py` – Loads insurance policy information.
- `report_generator.py` – Contains report-related functionality, if enabled in the current version.
- `policies/` – Stores insurance policy documents or related files.
- `frontend/` – Contains the React user interface, if maintained in this repository.

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible version supported by the dependencies
- PostgreSQL
- Node.js and npm, if running the React frontend
- Git
- An LLM provider configured for the application

### 1. Clone the Repository

```bash
git clone https://github.com/Priyadharshini134/priorr_agent.git
cd priorr_agent
```

### 2. Set Up the Python Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure the Database

Create a PostgreSQL database for the mock Electronic Health Record (EHR) system.

```sql
CREATE DATABASE ehr_db;
```

Configure the database connection details in the application's database configuration. Create the required tables and insert sample patient records and insurance policy data according to the project's schema.

### 4. Configure the LLM

Configure the LLM provider used by your current code. If the application uses Groq, set the required API key through an environment variable. If it uses Ollama, ensure Ollama is installed, the required model is available, and the service is running.

Do not commit API keys, passwords, or other credentials to GitHub.

### 5. Start the Backend

Run the FastAPI application using the module path that matches your project structure. For example, if `app/api.py` exposes the FastAPI instance named `app`:

```bash
uvicorn app.api:app --reload
```

Open Swagger UI in your browser:

```text
http://127.0.0.1:8000/docs
```

### 6. Start the Frontend

If the React frontend is present in the repository, open a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Ensure that the frontend's API base URL matches the address where the FastAPI backend is running.

## 🔌 API Usage

The backend exposes a prior authorization endpoint for processing a patient's authorization request.

**Endpoint:** `POST /prior-auth/{patient_id}`

**Example request:**

```http
POST http://127.0.0.1:8000/prior-auth/1
```

The request uses the patient ID to retrieve the corresponding patient record and initiate the workflow.

**Example response fields:**

```json
{
  "patient_record_text": "...",
  "clinical_summary": "...",
  "policy_text": "...",
  "policy_decision": "...",
  "authorization_form": "...",
  "final_decision": "..."
}
```

The values above illustrate the response structure; actual fields and output formats depend on the current API implementation.

You can test the endpoint through Swagger UI at `http://127.0.0.1:8000/docs`.

## 🧪 Example Use Case

Consider a patient diagnosed with rheumatoid arthritis who requires Humira treatment.

The system can:

1. Retrieve the patient's medical history and laboratory results.
2. Identify previous medication usage and relevant clinical findings.
3. Retrieve the applicable biologic therapy insurance policy.
4. Evaluate configured eligibility criteria, such as previous medication requirements and CRP levels.
5. Generate a structured authorization summary and decision based on the evaluation.

The final decision depends on the configured insurance policy rules and the available patient information.

## 🔐 Security and Limitations

- This project is a prototype intended for demonstration and development.
- Sample or synthetic patient data should be used for testing.
- Patient consent, access control, and audit logging must be implemented and validated before production use.
- Authorization decisions should be reviewed by qualified healthcare or insurance personnel.
- The system does not replace professional medical judgment or actual insurer approval.
- Production deployment requires appropriate privacy, security, regulatory, and reliability controls.

## 🚀 Future Enhancements

- Digital patient consent capture and verification.
- Dynamic insurance policy document extraction.
- Support for multiple insurance providers and policy formats.
- Improved workflow tracking and notifications.
- Role-based access control for healthcare providers and administrators.
- Comprehensive audit trails and decision explanations.
- Integration with real EHR and insurance systems.

## 👩‍💻 Author

**Priyadharshini M**

Computer Science and Business Systems

GitHub: [Priyadharshini134](https://github.com/Priyadharshini134)

## 📄 License

A license has not been specified here. Add a suitable license file if you intend to distribute or allow reuse of this project.
