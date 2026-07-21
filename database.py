import sqlite3
from config import DATABASE


# Create database and table
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    room TEXT,
    confidence REAL,
    length REAL,
    width REAL,
    height REAL,
    area REAL,
    style TEXT,
    budget REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")


# Save prediction
def save_prediction(
    room,
    confidence,
    length,
    width,
    height,
    area,
    style,
    budget
):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (room, confidence, length, width, height, area, style, budget)

    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        room,
        confidence,
        length,
        width,
        height,
        area,
        style,
        budget
    ))

    conn.commit()
    conn.close()


# Show all saved records
def show_predictions():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    show_predictions()