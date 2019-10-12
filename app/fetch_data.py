from app import app
import requests
import json
from .models import Source


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sources_url = f'https://newsapi.org/v2/sources?apiKey={app.config["NEWS_API_KEY"]}'

    res = requests.get(sources_url)
    sources_data = res.json().get('sources')
    return process_sources(sources_data)


def process_sources(sources_data):
    '''
    Function that converts source dict into source model
    '''
    sources = []
    for source_data in sources_data:
        source = Source(source_data['id'], source_data['name'], source_data['description'],
                        source_data['url'], source_data['category'], source_data['language'], source_data['country'])
        sources.append(source)
    return sources
