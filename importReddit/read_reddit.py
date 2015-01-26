import json
import urllib2
import pymongo


# esctablish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the reddit

db = connection.reddit
stories = db.stories

# get the reddit home page

reddit_page = urllib2.urlopen("http://www.reddit.com/r/Python/.json", timeout=60)

#parse the json into Python objects

parsed = json.loads(reddit_page.read())

# iterated throught every news item on the page

for item in parsed['data']['children']:
	# put it in mongodb
	stories.insert(item['data'])
	#print item['data']