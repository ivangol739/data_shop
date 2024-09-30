from dotenv import load_dotenv
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables


load_dotenv()
DSN = os.getenv('DSN')
engine = sqlalchemy.create_engine(DSN)


create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()
