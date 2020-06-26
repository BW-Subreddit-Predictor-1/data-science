import requests
import json


url = "http://localhost:5000/predict_subreddit" # if you want to test local
#url = "https://bwptphsp1ds.herokuapp.com/predict_subreddit"  # if you want to test deployed 

# this assumes that the agreed upon json keys are `title` and 'body' 
val = {'title': 'i want to learn data science', 'body': 'b'} 
r_success = requests.post(url, data=json.dumps(val))
print(f'url: {url}')
print(f"request responded: {r_success}.\nthe content of the response was {r_success.json()}")
# you'll get a 200 response if the keys align, and something bad if the keys don't align. 