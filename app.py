from flask import Flask, request,jsonify
from flask_cors import CORS 
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


app = Flask(__name__)
CORS(app)




def getSimilarityOfTwoString(str1, str2):
    embeddings = model.encode([str1, str2], convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    similarity_score = cosine_scores.item()
    
    return max(0, similarity_score)  # Ensuring similarity score is greater than 0

def getSimilarityOfArrayOfStrings(args):
    array_of_strings = args['data']
    str2 = args['rawText']
    callback = {}
    sortingOrder = args.get('sortingOrder', None)
    itemsToBeRendered = args.get('itemsToBeRendered', None)

    array_embeddings = model.encode(array_of_strings, convert_to_tensor=True)
    str2_embedding = model.encode(str2, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(array_embeddings, str2_embedding)

    similarity_scores = cosine_scores.tolist()

    result = []
    for i in range(len(array_of_strings)):
        similarity_scale = similarity_scores[i][0]
        if similarity_scale > 0:  # Filter out cases where similarity scale is 0
            result.append({
                "targetString": array_of_strings[i],
                "similarityScale": similarity_scale
            })

    if sortingOrder == 1:
        result.sort(key=lambda x: x['similarityScale'], reverse=True)
    else:
        result.sort(key=lambda x: x['similarityScale'])

    if itemsToBeRendered:
        result = result[:itemsToBeRendered]

   
    best_match = result[0] if result else None
    best_match_index = array_of_strings.index(best_match['targetString']) if best_match else None
    callback = {
        "bestMatch": best_match,
        "bestMatchIndex": best_match_index
    }

    return {result,callback}


def get_similarity_scale(obj, raw_text, matching_keys):
    similarity_scores = []
    for key in matching_keys:
        obj_text = str(obj.get(key, ''))
        similarity_score = getSimilarityOfTwoString(obj_text, raw_text)
        similarity_scores.append(similarity_score)

    average_similarity_scale = max(0, sum(similarity_scores) / len(similarity_scores)) if similarity_scores else 0

    return average_similarity_scale

def getSimilarityScaleofArrayOfObjects(args):
    data = args['data']
    raw_text = args['rawText']
    object_matching_keys = args['objectMatchingKeys']
    sorting_order = args.get('sortingOrder', None)
    items_to_be_rendered = args.get('itemsToBeRendered', None)

    result = []

    for obj in data:
        similarity_scale = get_similarity_scale(obj, raw_text, object_matching_keys)
        result.append({
            "item": obj,
            "similarityScale": similarity_scale,
            "averageSimilarityScale": similarity_scale
        })

    if sorting_order == 1:
        result.sort(key=lambda x: x['averageSimilarityScale'], reverse=True)
    elif sorting_order == 0:
        result.sort(key=lambda x: x['averageSimilarityScale'])

    if items_to_be_rendered:
        result = result[:items_to_be_rendered]

    return result

def getSimilarityofArrayOfObjects(args):
    data = args['data']
    raw_text = args['rawText']
    object_matching_keys = args['objectMatchingKeys']
    similarity_scale_threshold = args.get('similarityScaleThreshold', 0)
    sorting_order = args.get('sortingOrder', None)
    items_to_be_rendered = args.get('itemsToBeRendered', None)
    callback = {}

    result = []

    for idx, obj in enumerate(data):
        similarity_scale = get_similarity_scale(obj, raw_text, object_matching_keys)

        if similarity_scale > similarity_scale_threshold:  # Filter out cases below threshold
            result.append({
                "item": obj,
                "similarityScale": similarity_scale,
                "averageSimilarityScale": similarity_scale
            })

    if sorting_order == 1:
        result.sort(key=lambda x: x['averageSimilarityScale'], reverse=True)
    elif sorting_order == 0:
        result.sort(key=lambda x: x['averageSimilarityScale'])

    if items_to_be_rendered:
        result = result[:items_to_be_rendered]

    if  result:
        best_match = result[0]
        best_match_index = data.index(best_match['item'])
        callback = {
            "bestMatch": best_match,
            "bestMatchIndex": best_match_index
        }

    return {result,callback}



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
     print(temp)
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
     print(temp)
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
     print(temp)   
     return jsonify({"data":temp}), 200 

@app.route("/getSimilarityOfTwoString",methods=["POST"])
def getSimilarityOfTwoString_api():
    request_data = request.json
    string1 = request_data.get("string1")
    string2 = request_data.get("string2")
    temp = getSimilarityOfTwoString(string1,string2)

    if(temp):
     print(temp)   
     return jsonify({"data":temp}), 200           


if __name__ == "__main__":

    app.run(debug=True, use_reloader = False)