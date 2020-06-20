import pandas as pd


connection = 'postgres://ughwjzuswfudem:3740b6c26e6d05a122c39c0460fed884410295a226d6caf1a69fef567c13cafb@ec2-34-202-88-122.compute-1.amazonaws.com:5432/dc60bdmtqoftf5'

subreddits = pd.read_sql_table('subreddit', connection)
threads = pd.read_sql_table('thread', connection)

data = threads.merge(subreddits, left_on='subreddit', right_on='id')

data.columns = ['id', 'title', 'title_embedding', 'body', 'body_embedding', 'upvotes', 'del_1', 'del_2', 'subreddit']
data = data.drop(['del_1', 'del_2'], axis=1)
data.to_csv('data.csv')
print(data.head())