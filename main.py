from sqlalchemy.orm import Session

from engine.book import *


if __name__=='__main__':
    res = BookScraping.fetch_books(keyword="Python", max_results=40, page_count=10)
    print(res)