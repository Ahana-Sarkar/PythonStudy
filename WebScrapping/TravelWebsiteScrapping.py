from tkinter.filedialog import Open
from urllib import request
from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://rapidapi.com/blog/best-travel-websites/').text

content= BeautifulSoup(source, 'lxml')

csv_file= open('Travel_Website.csv', 'w')

csv_writer= csv.writer(csv_file)
csv_writer.writerow(['Name', 'Link'])

summary = content.find('div', class_="entry-content")
for results in summary.find_all('h3'):
    if results.a == None:
        break
    else:
        website_name = str(results.a.text)
        website_link = str(results.a)
        santinized_website_link = website_link.split('"')[1]
        print(website_name)
        print(website_link)
        print(santinized_website_link)
        csv_writer.writerow([website_name, santinized_website_link])

csv_file.close()
