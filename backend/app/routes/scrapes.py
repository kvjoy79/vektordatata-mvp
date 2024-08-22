from app import app
from flask import request, Blueprint
from app.helpers.apify_scraping import scrape_google_reviews

scrape_bp = Blueprint('scrape', __name__)
# /v1/api


@scrape_bp.route('/')
def test():
    return 'Scrape route'

@scrape_bp.route('/scrape-data', methods=['POST'])
def scrape_data():
    data = request.get_json()
    query = data['query'] 
    scraping_result = scrape_google_reviews(query)
    return {'message': 'Scraping completed successfully!'}