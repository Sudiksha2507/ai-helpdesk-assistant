"""
db.py
All MySQL access for the ticket management workflow.
"""

import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "appuser",
    "password": "apppass123",
    "database": "ai_helpdesk_assistant",
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def create_ticket(user_name: str, subject: str, question: str, assistant_reply: str) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO tickets (user_name, subject, question, assistant_reply, status)
           VALUES (%s, %s, %s, %s, 'OPEN')""",
        (user_name, subject, question, assistant_reply),
    )
    conn.commit()
    ticket_id = cur.lastrowid
    cur.close()
    conn.close()
    return ticket_id


def get_all_tickets() -> list:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM tickets ORDER BY created_at DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def update_ticket_status(ticket_id: int, status: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tickets SET status = %s WHERE id = %s", (status, ticket_id))
    conn.commit()
    cur.close()
    conn.close()
