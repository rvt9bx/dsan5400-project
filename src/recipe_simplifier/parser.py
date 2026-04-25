import cloudscraper
from recipe_scrapers import scrape_html
from recipe_simplifier.recipe import Recipe
import logging

logger = logging.getLogger(__name__)


def parse_url(url):
    """Scrape a recipe URL and return a Recipe object.

    Args:
        url (str): URL of the recipe page to scrape.

    Returns:
        Recipe: Parsed recipe containing title, ingredients, and instructions.

    Raises:
        Exception: If the page cannot be scraped or the recipe format is unrecognized.
    """

    # get html
    html_scraper = cloudscraper.create_scraper()
    html = html_scraper.get(url).text

    # scrape recipe
    try:
        recipe_scraper = scrape_html(html, org_url=url)
    except Exception as e:
        print("Recipe scraping failed, see logs/simplifier.logs for traceback.")
        logging.error(f"Recipe scraping failed: {e}")
        raise

    # get title, ingredients, instructions
    title = recipe_scraper.title()
    ingredients = recipe_scraper.ingredients()
    instructions = recipe_scraper.instructions()

    return Recipe(title, ingredients, instructions)
