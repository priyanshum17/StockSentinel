import requests
import certifi
from GoogleNews import GoogleNews
from sources.indianews import IndiaNews

requests.utils.DEFAULT_CA_BUNDLE_PATH = certifi.where()

API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	output = response.json()
	return output[0][0]['score']
	
def get_title(query):
	news = GoogleNews()
	news.search(query)
	return [story['title'] for story in news.results()]

def analysis(ticker):
	query_list = get_title(ticker)
	index = 0
	number = 0
	for query_title in query_list:
		index += query(query_title)
		number += 1
	
	ratio = index / number
	if ratio > 0.7:
		return 'Postive'
	elif ratio > 0.4:
		return 'Neutral'
	else:
		return 'Negative'

print(analysis('TSLA'))