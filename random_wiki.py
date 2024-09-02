import wikipediaapi
import random
import os
from dotenv import load_dotenv


load_dotenv()


def get_random_article_in_category(category_name, language="en"):

    user_agent = os.getenv("USER_AGENT")

    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent=user_agent,
        language=language,
    )
    category_page = wiki_wiki.page(f"Category:{category_name}")
    pages = list(category_page.categorymembers.values())
    articles = [page for page in pages if page.ns == 0]

    if articles:
        random_page = random.choice(articles)
        return random_page.title, random_page.summary
    else:
        return None, "No articles found in this category"


# Setting topic: "Software development"
title, summary = get_random_article_in_category("Software_development")
print(f"Title: {title}\nSummary: {summary}")
