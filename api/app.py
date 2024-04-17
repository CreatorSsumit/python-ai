from flask import Flask, request,jsonify
from flask_cors import CORS 
from api.main import getSimilarityOfTwoString,getSimilarityOfArrayOfStrings,getSimilarityScaleofArrayOfObjects,getSimilarityofArrayOfObjects



app = Flask(__name__)
CORS(app)

@app.route("/")
def home_route():
    return("hello from Home Page")

@app.route("/getSimilarityofArrayOfObjects",methods=["POST"])
def getSimilarityofArrayOfObjects_api():
    request_data = request.json
    new_data = {
        "data": request_data.get("data"),
        "rawText": request_data.get("rawText"),
        "objectMatchingKeys": request_data.get("objectMatchingKeys"),
        "similarityScale": request_data.get("similarityScale"),
        "sortingOrder": request_data.get("sortingOrder"),
        "itemsToBeRendered": request_data.get("itemsToBeRendered")
    }
    temp = getSimilarityofArrayOfObjects(new_data)

    if(temp):
     return jsonify({"data":temp}), 200   

@app.route("/getSimilarityScaleofArrayOfObjects",methods=["POST"])
def getSimilarityScaleofArrayOfObjects_api():
    request_data = request.json
    new_data = {
        "data": request_data.get("data"),
        "rawText": request_data.get("rawText"),
        "objectMatchingKeys": request_data.get("objectMatchingKeys"),
        "sortingOrder": request_data.get("sortingOrder"),
        "itemsToBeRendered": request_data.get("itemsToBeRendered")
    }
    temp = getSimilarityScaleofArrayOfObjects(new_data)

    if(temp):
     return jsonify({"data":temp}), 200 
    
@app.route("/getSimilarityOfArrayOfStrings",methods=["POST"])
def getSimilarityOfArrayOfStrings_api():
    request_data = request.json
    new_data = {
        "data": request_data.get("data"),
        "rawText": request_data.get("rawText"),
        "sortingOrder": request_data.get("sortingOrder"),
        "itemsToBeRendered": request_data.get("itemsToBeRendered")
    }
    temp = getSimilarityOfArrayOfStrings(new_data)

    if(temp):
     return jsonify({"data":temp}), 200 

@app.route("/getSimilarityOfTwoString",methods=["POST"])
def getSimilarityOfTwoString_api():
    request_data = request.json
    string1 = request_data.get("string1")
    string2 = request_data.get("string2")
    temp = getSimilarityOfTwoString(string1,string2)

    if(temp):
     return jsonify({"data":temp}), 200           


if __name__ == "__main__":

    app.run(debug=True, use_reloader = False)