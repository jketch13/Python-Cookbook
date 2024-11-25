import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Scrape COVID-19 data
def scrape_covid_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'main_table_countries_today'})

    headers = [th.text for th in table.find_all('th')]
    rows = []
    for tr in table.find_all('tr')[1:]:
        cols = [td.text.strip() for td in tr.find_all('td')]
        rows.append(cols)

    return pd.DataFrame(rows, columns=headers)


# Step 2: Process the data
def process_data(df):
    df = df[['Country,Other', 'TotalCases', 'TotalDeaths', 'TotalRecovered']]
    df = df.replace({'': '0', 'N/A': '0'}).fillna('0')
    df = df[df['Country,Other'] != '']
    df['TotalCases'] = df['TotalCases'].str.replace(',', '').astype(int)
    df['TotalDeaths'] = df['TotalDeaths'].str.replace(',', '').astype(int)
    df['TotalRecovered'] = df['TotalRecovered'].str.replace(',', '').astype(int)
    return df


# Step 3: Visualize the data
def plot_data(df):
    plt.figure(figsize=(15, 10))
    sns.barplot(x='TotalCases', y='Country,Other', data=df.nlargest(10, 'TotalCases'))
    plt.title('Top 10 Countries by Total COVID-19 Cases')
    plt.xlabel('Total Cases')
    plt.ylabel('Country')
    plt.show()


if __name__ == "__main__":
    url = 'https://www.worldometers.info/coronavirus/'
    df = scrape_covid_data(url)
    df = process_data(df)
    plot_data(df)
