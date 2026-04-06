import cloudscraper
from recipe_scrapers import scrape_html

def parse_url(url):
    '''function to take in a recipe url as a string and return the title, ingredient list, and instruction list '''
    
    # get html
    html_scraper = cloudscraper.create_scraper()
    html = html_scraper.get(url).text

    # scrape recipe
    recipe_scraper = scrape_html(html, org_url=url)

    # get title, ingredients, instructions 
    title = recipe_scraper.title()
    ingredients = recipe_scraper.ingredients()
    instructions = recipe_scraper.instructions()
    return title, ingredients, instructions

    # print("TITLE:", recipe_scraper.title())
    # print("\nINGREDIENTS:")
    # for i in recipe_scraper.ingredients():
    #     print("-", i)

    # print("\nINSTRUCTIONS:")
    # print(recipe_scraper.instructions())