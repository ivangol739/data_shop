from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


class Publisher(Base):
	__tablename__ = 'publisher'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)


class Book(Base):
	__tablename__ = 'book'
	id = Column(Integer, primary_key=True)
	title = Column(String, nullable=False)
	id_publisher = Column(Integer, ForeignKey('publisher.id'), nullable=False)
	publisher = relationship('Publisher', backref='books')


class Shop(Base):
	__tablename__ = 'shop'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)


class Stock(Base):
	__tablename__ = 'stock'
	id = Column(Integer, primary_key=True)
	id_book = Column(Integer, ForeignKey('book.id'), nullable=False)
	id_shop = Column(Integer, ForeignKey('shop.id'), nullable=False)
	count = Column(Integer, nullable=False)
	book = relationship('Book', backref='stocks')
	shop = relationship('Shop', backref='stocks')


class Sale(Base):
	__tablename__ = 'sale'
	id = Column(Integer, primary_key=True)
	price = Column(Float, nullable=False)
	date_sale = Column(DateTime, nullable=False)
	id_stock = Column(Integer, ForeignKey('stock.id'), nullable=False)
	count = Column(Integer, nullable=False)
	stock = relationship('Stock', backref='sales')


def create_tables(engine):
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)