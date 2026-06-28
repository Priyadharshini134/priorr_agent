from app.graph import graph

sample_record = """
Diagnosis: Chronic Migraine

Symptoms:
- Severe headaches for 6 months
- Failed medication therapy

Requested Procedure:
MRI Brain
"""

result = graph.invoke({
    "patient_record_text": sample_record
})

print(result)