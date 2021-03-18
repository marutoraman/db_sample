# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session,Session
import os
import ulid
from dotenv import load_dotenv
load_dotenv() #環境変数のロード

''' DBを使用するための準備 '''

SQLALCHEMY_DATABASE_URL = os.environ["DB_PATH"]
SQLALCHEMY_DATABASE_URL += '?charset=utf8mb4'
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=360,pool_size=100)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(bind=engine)
session = scoped_session(SessionLocal)

def get_ulid():
  return ulid.new().str
