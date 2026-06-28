import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ehr_db",
        user="postgres",
        password="Priya@123",
        port="5432",
        cursor_factory=RealDictCursor
    )


def get_policy(insurance_company, diagnosis, treatment):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM insurance_policies
        WHERE insurance_company=%s
        AND diagnosis=%s
        AND treatment=%s
    """, (insurance_company, diagnosis, treatment))

    policy = cursor.fetchone()

    cursor.close()
    conn.close()

    return policy


def get_policy_rules(policy_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT rule_name,
               operator,
               expected_value
        FROM policy_rules
        WHERE policy_id=%s
    """, (policy_id,))

    rules = cursor.fetchall()

    cursor.close()
    conn.close()

    return rules


def get_required_documents(policy_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT document_name
        FROM document_checklist
        WHERE policy_id=%s
    """, (policy_id,))

    docs = cursor.fetchall()

    cursor.close()
    conn.close()

    return docs