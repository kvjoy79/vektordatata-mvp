from app import app
from flask import render_template, request, jsonify
from app.helpers.apify_scraping import scrape_google_reviews

@app.route('/')
def test():
    return 'Hello, World!'

@app.route('/scrape-data', methods=['POST'])
def scrape_data():
    data = request.get_json()
    query = data['query']
    scraping_result = scrape_google_reviews(query)
    return {'message': 'Scraping completed successfully!'}