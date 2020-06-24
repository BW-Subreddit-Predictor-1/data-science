from flask import Blueprint, request, Flask, Response, stream_with_context
import pickle
import json


predict_subreddit_route = Blueprint('predict_subreddit_route', __name__)

encoder = pickle.load(open('encoder.pkl','rb'))
model = pickle.load(open('RFC_model.pkl','rb'))
vect = pickle.load(open('vect.pkl','rb'))

@predict_subreddit_route.route('/predict_subreddit', methods=['POST'])
def predict_subreddit():

     """Gets data in JSON format and runs it through the model.
       :return: JSON file.
    """
    data = request.get_json()
    text = data['text']
    features = {'text':text}

    # Converts the data into a DataFrame object.
    predict_data = pd.DataFrame(features,index[1])
    features_vectorizer = vect.transform(predict_data)

    # Feeds the data into the model.
    prediction = model.predict(features_vectorizer)
    pred_class = encoder.inverse_transform(prediction)

    return jsonify({'prediction_class': pred_class})
