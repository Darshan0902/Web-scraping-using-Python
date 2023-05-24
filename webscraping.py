import bs4 as bs
import requests

html = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup = bs.BeautifulSoup(html.text,'html.parser')

tickers = []

# Using the "find" generally returns all the table so as result I ensured that we include the only needed "table" instead of
# the whole page .
table = soup.find("table",{"class" : "wikitable sortable"})
rows = table.findAll('tr')[1:]

# Retrieving all the rows in table
for row in rows:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker[:-1])
    # [:-1] was used to remove the "/n" we will be recieving in outputs.

    print(tickers)