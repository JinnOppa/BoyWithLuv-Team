import requests
from bs4 import BeautifulSoup
import json

# Define the Shopee URL for iPhone 16 search results
url = 'https://shopee.com.my/search?keyword=iphone%2016'

# Set headers to mimic a real browser request (to avoid blocking)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the script tag that contains JSON data (Shopee usually returns data as JSON embedded in HTML)
data_script = soup.find('script', id='__NEXT_DATA__')

# Parse the JSON data
if data_script:
    data_json = json.loads(data_script.string)
    
    # Extract relevant data (e.g., product name, price, etc.)
    for item in data_json['props']['pageProps']['initialState']['searchItems']:
        product_name = item['name']
        price = item['price']
        rating = item['rating']
        print(f'Product: {product_name}, Price: {price}, Rating: {rating}')
