from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from tables.order_product import Order_Product

from base_template import Base, Session, engine

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key = True)
    order = relationship('Order_Product')
    price = Column(Float)
    date = Column(Date)
    worker_id = Column(Integer, ForeignKey('workers.id'))

    def __init__(self):
        self.order = []
        self.price = 0
        self.date = date.today()
    
    def add_product_to_order(self, product, amount):
        self.order.append((Order_Product(product, amount)))

    def count_price(self):
        self.price = 0
        for item_and_amount in self.order:
            item = item_and_amount.ordered_product
            amount = item_and_amount.amount
            for i in range(amount):
                self.price += item.price

    def finish_order(self, wallet):
        self.count_price()
        wallet.add_money(self.price)
        session = Session()
        session.add(self)
        session.commit()
        session.close()
Base.metadata.create_all(engine)