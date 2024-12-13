import os
import re
import requests
import pandas as pd
from lxml import html
from dotenv import load_dotenv
import constants
load_dotenv()

def get_parsed_response(search_text, page):
    url = os.getenv("base_url") + f'/{search_text}?page={page}'
    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully fetched the webpage.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        exit()
    return html.fromstring(response.content)

def get_total_pages(search_text):
    tree = get_parsed_response(search_text, 1)
    pagination_text = ''.join(tree.xpath(constants.PAGINATION))

    if pagination_text:
        match = re.search(r"of\s*(\d+)", pagination_text)
        if match:
            total_results = int(match.group(1))
            results_per_page = 20
            total_pages = (total_results // results_per_page) + (1 if total_results % results_per_page > 0 else 0)
            print(f"Total pages: {total_pages}")
        else:
            print("Could not find the total results in pagination text.")
            exit()
    else:
        print("Pagination information not found.")
        exit()
    return total_pages

def extract_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel(f'extracts/{os.getenv("search_text")}_data.xlsx', index=False)
    print(f"Data saved to '{os.getenv('search_text')}_data.xlsx'.")