### Simple URL scraper

Arguments:
```bash
python webscrap.py -h
usage: webscrap.py [-h] [--url URL] [--limit LIMIT] [--output OUTPUT]

URL scrapper

optional arguments:
  -h, --help       show this help message and exit
  --url URL        Root URL page
  --limit LIMIT    Limit urls to scrape
  --output OUTPUT  Path to output file
```

app usage:

```bash
python webscrap.py --url https://example.com --limit 10000 --output output.csv
```