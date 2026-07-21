from flask import Flask, render_template, request, send_file, redirect
from services.model_service import get_model
from services.prediction_service import predict_room
from services.history_service import (
    get_history,
    export_history_csv,
    delete_history_record
)
from services.report_service import generate_report
from services.database_service import save_room_prediction
from services.image_preprocess_service import save_and_preprocess_image
from services.interior_service import process_interior
from config import UPLOAD_FOLDER

import os
import sqlite3
import pandas as pd


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

model = get_model()

classes = [
    "bathroom",
    "bedroom",
    "home-office",
    "kitchen",
    "living-room",
    "pool"
]


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    top_predictions = None
    length = None
    width = None
    height = None
    area = None
    style = None
    recommendation = None
    furniture = None
    total_budget = None
    prompt = None
    generated_image = None
    uploaded_image = None

    if request.method == "POST":

        file = request.files["image"]

        filepath, uploaded_image, img_array = save_and_preprocess_image(file)

        prediction, confidence, top_predictions = predict_room(
            model,
            img_array,
            classes
        )

        length = request.form.get("length")
        width = request.form.get("width")
        height = request.form.get("height")
        style = request.form.get("style")

        if length and width:
            area = round(float(length) * float(width), 2)

        (
    recommendation,
    furniture,
    total_budget,
    prompt,
    generated_image
) = process_interior(
    prediction,
    style,
    area,
    height
)

        if prediction and recommendation and furniture:
            generate_report(
                prediction,
                confidence,
                length,
                width,
                height,
                area,
                style,
                recommendation,
                furniture,
                total_budget,
                prompt
            )

            save_room_prediction(
                prediction,
                confidence,
                length,
                width,
                height,
                area,
                style,
                total_budget
            )

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        top_predictions=top_predictions,
        length=length,
        width=width,
        height=height,
        area=area,
        style=style,
        recommendation=recommendation,
        prompt=prompt,
        furniture=furniture,
        total_budget=total_budget,
        generated_image=generated_image,
        uploaded_image=uploaded_image
    )


@app.route("/download")
def download_report():
    return send_file(
        "outputs/interior_report.pdf",
        as_attachment=True
    )


@app.route("/export_csv")
def export_csv():

    output_path = export_history_csv()

    return send_file(
        output_path,
        as_attachment=True
    )


@app.route("/delete/<int:id>")
def delete_prediction(id):

    delete_history_record(id)

    return redirect("/history")


@app.route("/history")
def history():

    search = request.args.get("search", "")

    data, total_predictions, room_counts, average_budget = get_history(search)

    return render_template(
        "history.html",
        records=data,
        total_predictions=total_predictions,
        room_counts=room_counts,
        average_budget=average_budget,
        search=search
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)