from flask import Flask, request, jsonify
from flask_cors import CORS
from main import (
    getSimilarityOfTwoString,
    getSimilarityOfArrayOfStrings,
    getSimilarityScaleofArrayOfObjects,
    getSimilarityofArrayOfObjects,
)

app = Flask(__name__)
CORS(app)


@app.route("/")
def home_route():
    return "Hello from Home Page"


def process_request(data, *args):
    request_data = request.json
    new_data = {key: request_data.get(key) for key in data}
    temp = args[0](new_data) if args else None
    return jsonify({"data": temp}), 200 if temp else 400


@app.route("/getSimilarityofArrayOfObjects", methods=["POST"])
def get_similarity_of_array_of_objects_api():
    return process_request(["data", "rawText", "objectMatchingKeys", "similarityScale", "sortingOrder", "itemsToBeRendered"], getSimilarityofArrayOfObjects)


@app.route("/getSimilarityScaleofArrayOfObjects", methods=["POST"])
def get_similarity_scale_of_array_of_objects_api():
    return process_request(["data", "rawText", "objectMatchingKeys", "sortingOrder", "itemsToBeRendered"], getSimilarityScaleofArrayOfObjects)


@app.route("/getSimilarityOfArrayOfStrings", methods=["POST"])
def get_similarity_of_array_of_strings_api():
    return process_request(["data", "rawText", "sortingOrder", "itemsToBeRendered"], getSimilarityOfArrayOfStrings)


@app.route("/getSimilarityOfTwoString", methods=["POST"])
def get_similarity_of_two_string_api():
    request_data = request.json
    string1, string2 = request_data.get("string1"), request_data.get("string2")
    temp = getSimilarityOfTwoString(string1, string2)
    return jsonify({"data": temp}), 200 if temp else 400


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
