from flask import Flask, request, jsonify
from flask_cors import CORS

from data.data_handler import DataHandler
from model.assigner import MedSocShuffle

ALLOWED_EXTENSIONS = {"csv"}

app = Flask(__name__)
app.config.from_object(__name__)
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
        data_handler = DataHandler(file_obj=file)
        people_array = data_handler.get_people_array()

        med_soc_shuffle = MedSocShuffle(people_array)
        assignments = med_soc_shuffle.run()

        return jsonify({"message": "Shuffled!", "assignments": assignments}), 200
    else:
        return jsonify({"error": "Invalid file type"}), 400


if __name__ == "__main__":
    app.run()
