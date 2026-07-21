import sqlite3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
import pandas as pd







def get_history(search=""):

    conn = sqlite3.connect("interior.db")
    cursor = conn.cursor()

    # Search
    if search:
        cursor.execute(
            "SELECT * FROM predictions WHERE room LIKE ? ORDER BY id DESC",
            (f"%{search}%",)
        )
    else:
        cursor.execute(
            "SELECT * FROM predictions ORDER BY id DESC"
        )

    data = cursor.fetchall()

    # Total Predictions
    cursor.execute("SELECT COUNT(*) FROM predictions")
    total_predictions = cursor.fetchone()[0]

    # Room Counts
    cursor.execute(
        "SELECT room, COUNT(*) FROM predictions GROUP BY room"
    )

    room_counts = cursor.fetchall()

    # Chart
    if room_counts:

        rooms = [row[0] for row in room_counts]
        counts = [row[1] for row in room_counts]

        os.makedirs("static/charts", exist_ok=True)

        plt.figure(figsize=(5,5))
        plt.pie(
            counts,
            labels=rooms,
            autopct="%1.1f%%"
        )

        plt.title("Room Distribution")

        plt.savefig(
            "static/charts/room_distribution.png"
        )

        plt.close()

    # Average Budget
    cursor.execute(
        "SELECT AVG(budget) FROM predictions"
    )

    average_budget = cursor.fetchone()[0]

    conn.close()

    return (
        data,
        total_predictions,
        room_counts,
        average_budget
    )



def export_history_csv():

    conn = sqlite3.connect("interior.db")

    df = pd.read_sql_query(
        "SELECT * FROM predictions",
        conn
    )

    conn.close()

    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/prediction_history.csv"

    df.to_csv(output_path, index=False)

    return output_path


def delete_history_record(record_id):

    conn = sqlite3.connect("interior.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM predictions WHERE id=?",
        (record_id,)
    )

    conn.commit()
    conn.close()
