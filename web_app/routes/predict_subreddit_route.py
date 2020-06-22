from flask import Blueprint, request, Flask, Response, stream_with_context
import pickle
import json


predict_subreddit_route = Blueprint('predict_subreddit_route', __name__)

@predict_subreddit_route.route('/predict_subreddit', methods=['POST'])
def predict_subreddit():
    '''a route that expects json object with 2 keys'''

    # receive input
    lines = request.get_json(force=True)

    # get data from json
    title_text = lines['title']
    body_text = lines['body']
    '''
    # deserialize pretrained model
    with open('model.pickle', 'rb') as mod:
        model = pickle.load(mod)

    # predict
    output = model.predict([[title_text, body_text]])
    '''
    # using dictionary to format output for json
    # send_back = {'prediction': output}
    send_back_placeholder = {'subreddit': 'placeholder'}
    send_back_dummy = {'dummy': 1}
    send_back_input = {
        'title': title_text,
        'body': body_text
    }

    # give output to sender
    return Response(
        response=json.dumps(send_back_placeholder),
        status=200,
        mimetype='application/json'
    )