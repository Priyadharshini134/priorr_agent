import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host="localhost",
    database="ehr_db",
    user="postgres",
    password="Priya@123",
    port="5432"
)

cursor = conn.cursor(cursor_factory=RealDictCursor)

def get_patient(patient_id):

    # Patient Details
    cursor.execute("""
        SELECT patient_name,
               age,
               gender,
               diagnosis,
               medication,
               provider_name
        FROM patients
        WHERE patient_id=%s
    """,(patient_id,))

    patient = cursor.fetchone()

    if not patient:
        return None

    # Clinical Notes
    cursor.execute("""
        SELECT note_text
        FROM clinical_notes
        WHERE patient_id=%s
    """,(patient_id,))

    notes = cursor.fetchall()

    # Lab Reports
    cursor.execute("""
        SELECT test_name,result
        FROM lab_reports
        WHERE patient_id=%s
    """,(patient_id,))

    labs = cursor.fetchall()

    # Prior Authorization History
    cursor.execute("""
    SELECT
        treatment_requested,
        insurance_provider,
        status
    FROM prior_auth_requests
    WHERE patient_id=%s
    """, (patient_id,))

    history = cursor.fetchall()

    cursor.execute("""

    SELECT observation_name,observation_value

    FROM patient_observations

    WHERE patient_id=%s

    """,(patient_id,))

    rows = cursor.fetchall()

    observations = {}

    for row in rows:

        observations[row["observation_name"]] = row["observation_value"]

    return {

        "patient":patient,

        "notes":notes,

        "labs":labs,

        "history":history,

        "observations":observations

    }