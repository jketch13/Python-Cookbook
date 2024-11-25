import requests
from bs4 import BeautifulSoup
import pandas as pd


# Function to fetch apartment listings
def fetch_apartments(zip_code):
    url = f"https://www.example-apartments.com/search?zip={zip_code}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    listings = soup.find_all('div', class_='listing')

    data = []
    for listing in listings:
        title = listing.find('h2', class_='title').text.strip()
        price = listing.find('div', class_='price').text.strip()
        size = listing.find('div', class_='size').text.strip()
        link = listing.find('a', href=True)['href']
        data.append([title, price, size, link])

    return pd.DataFrame(data, columns=['Title', 'Price', 'Size', 'Link'])


# Function to compare apartments
def compare_apartments(df):
    # Convert price to numeric value
    df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(float)
    # Convert size to numeric value
    df['Size'] = df['Size'].str.replace(' sqft', '').astype(int)

    # Sort by price and size
    df_sorted = df.sort_values(by=['Price', 'Size'], ascending=[True, False])

    return df_sorted


# Main function
if __name__ == "__main__":
    zip_code = '12345'  # Replace with your desired zip code
    df = fetch_apartments(zip_code)
    df_sorted = compare_apartments(df)

    print(df_sorted)
