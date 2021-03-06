from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from tools import string_to_object_from_table
from tables.stock import Stock

from base_template import Base

class Recipe(Base):
    '''
    Table connecting product's recipe
    with stock and adding amount of ingredient 
    '''
    __tablename__ = 'recipes'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'), primary_key = True)
    ingredient = relationship('Stock')
    amount = Column(Integer)

    def __init__(self, ingredient, amount):
        '''
        Adds data to table

        Parameters:
            ingredient (str): Name of the stock item to be used in recipe
            amount (int): Amount of ingredient
        '''
        self.amount = amount
        self.ingredient = string_to_object_from_table(ingredient, Stock)

    def __repr__(self):
        return self.ingredient.__repr__()