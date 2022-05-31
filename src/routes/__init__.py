from flask import Blueprint
from src.routes.verification import verification

# Hub for all the various routes that will be added to the app.
api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(verification.verification_bp)

# Main blueprint for the API route.
@api_blueprint.route("/", methods=["GET"])
def get_data():
    return """
        <html>
            <head>
                <style>
                    table, th, td \u007b
                        border: 1px solid black;
                        padding: 15px;
                        \u007d
                    tr:hover {background-color: #D6EEEE;}
                </style>
                <title>Dyte Internship Assignment</title>
            </head>
            <body>
                <h1>API Documentation<h1>
                <table>
                <thead>
                    <tr>
                        <th>Endpoint</th>
                        <th>Method</th>
                        <th>Parameters</th>
                        <th>Description</th>
                        <th>Example</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>/api/verify</td>
                        <td>POST</td>
                        <td>Key</td>
                        <td>Application runs here. Use API Key to access it</td>
                        <td><a href="https://dyte-internship.herokuapp.com/api/verify?key=51A3AF9D1148C7CB29138A9DD4CD1C67">https://dyte-internship.herokuapp.com/api/verify?key=API_KEY</td>
                    </tr>
                </tbody>
                </table>
            </body>
        </html>
        """
