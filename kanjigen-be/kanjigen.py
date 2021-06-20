from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route("/", methods=["POST"])
def upload_file():
    files = request.files

    inputfile = files["inputfile"].read().decode("utf-8")
    outputfile = files["outputfile"].read().decode("utf-8")
    print(inputfile)
    print(outputfile)
    return jsonify({"data": inputfile})
