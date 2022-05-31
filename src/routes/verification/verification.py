from flask import Flask, current_app, jsonify, request, Blueprint
from werkzeug.utils import secure_filename
from src.components.verify import verify
import csv
import os

UPLOAD_FOLDER = "temp"
ALLOWED_EXTENSIONS = {"csv"}
verification_bp = Blueprint("verification", __name__, url_prefix="/verify")


@verification_bp.route("/", methods=["GET", "POST"])
def verification():
    current_app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if request.method == "POST":
        key = request.args.get("key")
        if not key == os.getenv("API_KEY"):
            return "Unauthorized: Invalid API Key", 401
        if "file" not in request.files:
            return (
                "ERROR: File not found. Please upload a CSV file containing details",
                400,
            )
        file = request.files["file"]
        filename = file.filename
        dependency = request.form["dependency"]
        version = request.form["version"]
        if filename == "":
            return "ERROR: File not found.", 400
        if (
            dependency == ""
            or version == ""
            or dependency == "Enter Dependancy Here"
            or version == "Enter Version Here"
        ):
            return "ERROR: Dependency and version cannot be empty.", 400
        allowed_file = "." in filename and filename.rsplit(".", 1)[1].lower() in {"csv"}
        if file and allowed_file:
            filename = secure_filename(filename)
            file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            try:
                result = verify(
                    f"{UPLOAD_FOLDER}/{filename}",
                    request.form["dependency"],
                    request.form["version"],
                )
            except:
                return (
                    "ERROR: Make sure to follow exact structure as provided in examples/ebDetails.csv",
                    400,
                )
            return result
        else:
            return ("ERROR: Only CSV files are allowed", 400)
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h2>Provide Required Data</h2>
    <form method=post enctype=multipart/form-data>
        <input type=text name=dependency value="Enter Dependency Here"> <br> <br>
        <input type=text name=version value="Enter Version Here"> <br> <br>
        <input type=file name=file> <br> <br>
        <input type=submit value=Upload>
    </form>
    """
