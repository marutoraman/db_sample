# -*- coding: utf-8 -*-
from datetime import datetime as dt
from datetime import timedelta as delta
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, Boolean, func,update
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from pytz import timezone

from common.database import Base, get_ulid,session
from common.logger import set_logger
from common.utility import now_timestamp

class BookItem(Base):
    ''' Bookテーブル用 '''
    __tablename__ = 'book'
    mysql_charset='utf8mb4',
    mysql_collate='utf8mb4_unicode_ci'
    
    id = Column('id', Integer, primary_key=True)
    title = Column('title',String(100),nullable=False)
    isbn = Column('isbn',String(20),nullable=False)
    jan = Column('jan',String(20),nullable=True)
    author = Column('author',String(20),nullable=False)
    description = Column('description',String(1024),nullable=True)
    