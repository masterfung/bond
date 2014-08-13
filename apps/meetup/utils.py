from json import dumps, loads
from requests import get

# Create your views here.

meetup_api_key = "67f634b2a311c1b104c2c2e45d3856"
def meetup_api_find_topic():
	resp = get("https://api.meetup.com/topics.json",
		params={
			"key": meetup_api_key,
			"name": "javascript",
		},
	)

	if resp.status_code != 200:
		print "error"
		return

	print dumps(resp.json(), indent=2, sort_keys=True)
	print 'description:', resp.json()['meta']['description']


meetup_api_find_topic()

def meetup_api_find_open_events():
	resp = get("https://api.meetup.com/2/open_events.json",
		params={
			"key": meetup_api_key,
			"city": "san francisco",
			"state": "ca",
		    "country": "us",
			# "topic": "python",
		},
	)

	if resp.status_code != 200:
		print "error"
		return

	print dumps(resp.json(), indent=2, sort_keys=True)

meetup_api_find_open_events()

# /Users/htm/Desktop/RocketU/PycharmProjects/'Class Test'/'My Own Self Practice'/meetuptest.py