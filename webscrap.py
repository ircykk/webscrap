import requests
import time
import argparse
import sys
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

def fetch_urls(page):
	r = requests.get(page)
	soup = BeautifulSoup(r.text, 'lxml')
	for a in soup.find_all('a', href=True):
		url = a.get('href')

		# http://example.com == http://example.com/
		url = url.rstrip('/')

		if is_url(url) and url not in urls:
			urls.append(url)

def print_progress (iteration, total):
    print('\r%s/%s [%s...]' % (iteration, total, urls[-1][:64]), end = '\r')

# Instantiate the parser
parser = argparse.ArgumentParser(description='URL scrapper')
parser.add_argument('--url', help='Root URL page')
parser.add_argument('--limit', type=int, default=1000, help='Limit urls to scrape')
parser.add_argument('--output', default='output.csv', help='Path to output file')
args = parser.parse_args()

urls = []
urls_visited = []

if is_url(args.url) != True:
	print('Invalid root URL [--url]')
	sys.exit(1)

fetch_urls(args.url)
urls_visited.append(args.url);

for url in urls:
	if len(urls) > args.limit:
		break

	print_progress(len(urls), args.limit)

	if url not in urls_visited:
		urls_visited.append(url);
		fetch_urls(url)

# Save output
os.remove(args.output)
with open(args.output, 'a') as output:
	for url in urls:
	    output.write(url + '\n')
