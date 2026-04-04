
from urllib.request import urlopen
from recipe_scrapers import scrape_html

def parse_url():
    
    url = "https://www.allrecipes.com/lazy-girl-marinara-recipe-11933446"
    html = urlopen(url).read().decode("utf-8")  # retrieves the recipe webpage HTML
    # scraper = scrape_html(html, org_url=url)

    # # Extract recipe information
    # scraper.title()
    # scraper.instructions()
    # scraper.links()
    # scraper.to_json()
    # print(scraper.to_json())