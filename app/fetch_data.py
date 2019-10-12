from app import app
import requests, json

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sources_url = f'https://newsapi.org/v2/sources?apiKey={app.config["NEWS_API_KEY"]}'

    res = requests.get(sources_url)
    sources_data = res.json().get('sources')
    return sources_data