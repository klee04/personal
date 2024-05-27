import bs4 as bs
import requests
import csv 
import pandas as pd

scraped_page = requests.get('https://quotes.toscrape.com/')
page = bs.BeautifulSoup(scraped_page.text, "html.parser")

quotes = page.find_all('span', attrs={'class': 'text'})
author = page.find_all('small', attrs={'class': 'author'})

file = open("scraped_quotes.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow(['Quote', 'Author'])

for quote, author in zip(quotes, author):
    print(quote.text + ' - ' + author.text)
    writer.writerow([quote.text, author.text])
    
file.close()

tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

print(tables[0])



