import sqlite3

DB_NAME = "travel.db"

travel_tips = [
    "Keep digital copies of important documents.",
    "Pack light and leave space for souvenirs.",
    "Always carry a reusable water bottle.",
    "Check local customs before you travel.",
    "Keep emergency contacts saved offline.",
    "Arrive at the airport early for international flights.",
    "Carry essential medicines in your hand luggage.",
    "Inform your bank before international travel.",
    "Keep some local currency for emergencies.",
    "Label your luggage clearly with contact details."
]

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS travel_tips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tip TEXT NOT NULL
    )
    """)

    cursor.executemany(
        "INSERT INTO travel_tips (tip) VALUES (?)",
        [(tip,) for tip in travel_tips]
    )

    conn.commit()
    conn.close()

    print(f"Database '{DB_NAME}' created and populated successfully.")

if __name__ == "__main__":
    create_db()
