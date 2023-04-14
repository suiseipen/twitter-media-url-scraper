import requests
import json

authorization_key = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'

def guest_key():
	headers = {
		'authorization': authorization_key,
		}
	response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
	guest_token = response.json()["guest_token"]
	return guest_token

def video_url(tweet_id):
	api_url = 'https://api.twitter.com/1.1/statuses/show/%s.json' % tweet_id
	headers = {
		'authorization': authorization_key,
		'x-guest-token': guest_key()
		}
		
	data = {
		'cards_platform': 'Web-12',
		'include_cards': 1,
		'include_reply_count': 1,
		'include_user_entities': 0,
		'tweet_mode': 'extended',
		}
		
	res = requests.get(api_url, data=data, headers=headers)
	tweet_data = res.json()
	ex_entities = tweet_data['extended_entities']["media"][0]["video_info"]["variants"][3]["url"]
	return ex_entities
	
