# import sqlite3

# conn = sqlite3.connect(
# "prior_auth.db",
# check_same_thread=False
# )

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS requests(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# patient_name TEXT,
# decision TEXT,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# """)

# conn.commit()

# def save_request(name, decision):


# cursor.execute(
#     """
#     INSERT INTO requests
#     (
#         patient_name,
#         decision
#     )
#     VALUES (?, ?)
#     """,
#     (name, decision)
# )

# conn.commit()


