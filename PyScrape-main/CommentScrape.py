import datetime
import requests
'''
SEARCHES REDDIT COMMENT SECTIONS FOR STRING VARIBLES, AND RETURNS COMMENTS THAT CONTAIN SAID STRING 
EXAMPLE CODE WILL SEARCH R/GUITAR FOR EVERY MENTION OF STRINGS AND PRINT RESULT, ADDITIONAL TERMS CAN BE ADDED TO NARROW SEARCH RESULTS 
using pushshift.io api
----------------------------
q = Search term, string
ids = Get specific comments via their ids, Comma-delimited base36 ids
size = Number of results to return, Integer <= 500
fields = One return specific fields
sort = Sort results in a specific order,"asc", "desc"
sort_type = Sort by a specific attribute, "created_utc","score","num_comments", "created_utc"
aggs = Return aggregation summary,["author", "link_id", "created_utc", "subreddit"]
author = Restrict to a specific author, String
subreddit = Restrict to a specific subreddit, String
after = Return results after this date,Epoch value or Integer + "s,m,h,d" (i.e. 30d for 30 days)
before = Return results before this date, Epoch value or Integer + "s,m,h,d" (i.e. 30d for 30 days)
frequency = Used with the aggs parameter when set to created_utc,"second", "minute", "hour", "day"
metadata = display metadata about the
'''
class comment:
    def __init__(self, author, body, subreddit, score, created_utc, parent):
        self.author = author
        self.body = body
        #self.permalink = permalink
        self.subreddit = subreddit
        self.score = score
        self.timestamp = created_utc
        self.parent_id = parent
def get_list():
    global query, size, subreddit, sort_type, sort
    comment_list = []
    api_request = 'https://api.pushshift.io/reddit/search/comment/?q={0}&size={1}&subreddit={2}&sort_type={3}&sort={4}'.format((query),size,subreddit,sort_type,sort)
    client = requests.get(api_request)
    client.close()
    json_response = client.json()['data']

    for item in json_response:
        comment_list.append(comment(item['author'], str.lower(item['body']), item['subreddit'], item['score'], item['created_utc'], item['parent_id']))

    return comment_list
def print_list(list):
    counter = 1
    query_terms = query.split()

    for comment in list:
        timestamp = datetime.datetime.fromtimestamp(comment.timestamp)
        for term in query_terms: # make query terms bold
            if term in comment.body:
                string_start = comment.body.index(term)
                string_end = string_start + len(term)
                comment.body = comment.body[:string_start] + str('\033[1m' + term + '\033[0m') + comment.body[string_end:]

        print('╒═','#',counter,('═'*50),comment.score,'\\',timestamp.date(),sep='')
        print(' ',comment.body)
        counter = counter + 1

query = 'strings' # searched term, required

size = 250 # number of results to return, max 250
subreddit = 'guitar' # subreddit to search
sort = 'desc' # orders results
sort_type = '' # determins where to grab results from, newset,oldest, etc


print_list(get_list())