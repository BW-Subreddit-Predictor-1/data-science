# data-science
Our project uses NLP techniques to predict a subreddit for a user to post to

you can access the api by:

at the address `https://bwptphsp1ds.herokuapp.com`, along the route `predict_subreddit`, please send the
object `{'title': 'whatever the title is', 'body': 'whatever the body is'}
along a 200, you will receive the object {'subreddit': 'whatever subreddit is predicted'}


you can test that the api works by running the testing_predict_subreddit_route.py