"""App DB access for the audit log: who asked what, what SQL ran, what came back, when.
This is your compliance record — kept here, never mixed into the business DB.

TODO: log_query(user_id, question, generated_sql, result_row_count, timestamp)
"""
