from flask import Blueprint, request, Flask, Response
import pickle
import json
import os



predict_subreddit_route = Blueprint('predict_subreddit_route', __name__)

@predict_subreddit_route.route('/predict_subreddit', methods=['POST'])
def predict_subreddit():
    '''a route that expects json object with 2 keys'''

    # receive input
    lines = request.get_json(force=True)

    # get data from json
    title_text = lines['title']
    body_text = lines['body']
    
    # loading pickle files
    encoder_path = os.path.join(os.path.dirname(__file__), '..', '..', 'NLP', 'encoder.pkl')
    model_path =os.path.join(os.path.dirname(__file__), '..', '..', 'model.pkl')

    encoder = pickle.load(open(encoder_path, 'rb'))
    model = pickle.load(open(model_path, 'rb'))

    # using the pickle files to make prediction
    pred = model.predict([title_text])
    output = encoder.inverse_transform(pred)
    print(output)

    # using dictionary to format output for json
    send_back = {'subreddit': output[0]}
    
    # can swap the variable in the response to one of these for testing
    send_back_placeholder = {'subreddit': 'placeholder'}
    send_back_dummy = {'dummy': 1}
    send_back_input = {
        'title': title_text,
        'body': body_text
    }

    # give output to sender
    return Response(
        response=json.dumps(send_back),
        status=200,
        mimetype='application/json'
    )