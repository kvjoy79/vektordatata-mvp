from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()


def scrape_google_reviews(search_query):   
    """
    This function scrapes Google reviews for a given search query.
    
    Parameters:
    search_query (str): The search query for which the reviews are to be scraped.
    
    """ 
    client = ApifyClient(os.getenv('APIFY_TOKEN'))

    # Prepare the Actor input
    run_input = {
        "search_queries": [search_query],
        "scrape_name": True,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("runtime_terror/google-search-reviews-scraper").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items(limit=300):
        print(item)


