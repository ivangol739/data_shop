from dotenv import load_dotenv
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Sale, Stock, Shop
import json


def load_data():
	with open('fixtures/tests_data.json', 'r', encoding='utf-8') as f:
		data = json.load(f)

	for record in data:
		model = {
			'publisher': Publisher,
			'shop': Shop,
			'book': Book,
			'stock': Stock,
			'sale': Sale,
		}[record.get('model')]

		session.add(model(id=record.get('pk'), **record.get('fields')))
		session.commit()

def find_by_publisher(publisher_name):
	res = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
		.join(Stock, Stock.id_book == Book.id)\
		.join(Sale, Sale.id_stock == Stock.id)\
		.join(Shop, Stock.id_shop == Shop.id)\
		.join(Publisher, Book.id_publisher == Publisher.id).filter(Publisher.name == publisher_name).all()
	if not res:
		print("Ничего не найдено")
	else:
		for title, name, price, date_sale in res:
			print(f"{title} | {name} | {price} | {date_sale}")


if __name__ == "__main__":
	load_dotenv()
	DSN = os.getenv('DSN')
	engine = sqlalchemy.create_engine(DSN)
	create_tables(engine)
	Session = sessionmaker(bind=engine)
	session = Session()
	load_data()
	publisher_name = input("Введите автора:")
	find_by_publisher(publisher_name)
	session.close()
