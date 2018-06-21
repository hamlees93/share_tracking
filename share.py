import urllib.request
import bs4 as bs 
import csv
from datetime import datetime

class AppURLopener(urllib.request.FancyURLopener):
	"""Class creates a bypass to mod_security, allowing you 
	to access more websites"""
	version = "Mozilla/5.0"

opener = AppURLopener()

#get the page source of desired url
response = opener.open('https://hotcopper.com.au/').read()

#turns it into a beautiful soup product
soup = bs.BeautifulSoup(response, 'lxml')

#gets rid of symbols, so theres no issue with unicode
yourstring = soup.encode('ascii', 'ignore').decode('ascii')

#prints out data from the top 12 gainers of the day
gainers_data = soup.find(id='gainers')
gainers = gainers_data.text
print(gainers)

#opens a csv file with append, so old data will not be erased
#with open('index.csv','a') as csv_file:
#	writer = csv.writer(csv_file)
#	writer.writerow([gainers, datetime.now()])
