import os
from pathlib import Path
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS

from data.data_handler import DataHandler
from model.assigner import MedSocShuffle

UPLOAD_FOLDER = Path(__file__).parent / "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    print(f"Creating {UPLOAD_FOLDER} directory")
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {"csv"}

app = Flask(__name__)
app.config.from_object(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected for uploading"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    data_handler = DataHandler(
        frame_dir=os.path.join(app.config["UPLOAD_FOLDER"], filename)
    )
    people_array = data_handler.get_people_array()

    med_soc_shuffle = MedSocShuffle(people_array)
    assignments = med_soc_shuffle.run()

    return jsonify({"message": "Shuffled!", "assignments": assignments}), 200


if __name__ == "__main__":
    app.run()
