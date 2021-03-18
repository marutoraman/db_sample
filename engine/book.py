import os
import requests
import re
import time
from common.database import SessionLocal
from common.utility import *
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc

from models.book import *

# GooleBooksAPI
GOOGLE_BOOK_SEARCH_API = "https://www.googleapis.com/books/v1/volumes"

class BookScraping():
    ''' GoogleBooksAPIで本の情報を取得してDBに格納する '''
    
    @staticmethod
    def fetch_books(keyword:str, max_results:int, page_count:int=1):
        item_list=[]
        params = {
            "q":keyword,
            "maxResults": max_results if max_results <= 40 else 40,
        }
        item_list = []
        
        # セッション開始
        db:Session = SessionLocal()
        for page in range(page_count):
            params["startIndex"] = page * max_results
            res = requests.get(GOOGLE_BOOK_SEARCH_API,params=params)
            if res.status_code > 300:
                return item_list
            
            data = res.json()
            if not data.get("items"):
                return False
            for item in data.get("items"):
                try:
                    title = item["volumeInfo"]["title"]
                except:
                    title = ""
                try:
                    identifier = item["volumeInfo"]["industryIdentifiers"][0]["identifier"]
                except:
                    identifier = ""
                try:
                    description = item["volumeInfo"]["description"]
                except:
                    description = ""
                try:
                    authors = item["volumeInfo"]["authors"][0]
                except:
                    authors = ""
                # Insert
                db.add(BookItem(title=title, isbn=identifier, description=description, author=authors))

        # 保存確定
        db.commit()
            
        return item_list
    
                