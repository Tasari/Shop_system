from sqlalchemy import String, Integer, Column, Numeric
from sqlalchemy.orm import relationship
from tables.recipes import Recipe
from tools import name_changer, string_to_object_from_table
from tables.stock import Stock

from base_template import Base, Session 

class Product(Base):
    '''
    Table holding products
    '''
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True)
    price = Column(Numeric(scale=2))
    recipe = relationship('Recipe', backref='products')

    def __init__(self, name, price):
        '''
        Creates product normalizing the name
        Parameters:
            name (str): String representing the name of product
            price (float): Buying price of product
        '''
        self.name = name_changer(name)
        self.price = price
        self.recipe = []

    def add_ingredient_to_recipe(self, ingredient, amount):
        '''
        Adds ingredient to the recipe, containing given ingredient and amount
        Parameters:
            ingredient (str): String representing the name of ingredient
            amount (int): Amount of ingredient used in recipe
        '''
        self.recipe.append((Recipe(ingredient, amount)))

    def remove_ingredients_from_stock(self):
        '''
        Removes ingredients of every item from
        stock based on recipe
        '''
        session = Session()
        recipe = session.query(Recipe).\
            filter(Recipe.product_id == self.id).\
                all()

        for ingredient_and_amount in recipe:
            ingredient = ingredient_and_amount.ingredient
            amount = ingredient_and_amount.amount
            stock = string_to_object_from_table(ingredient.name, Stock)
            ingredient.update_object_quantity_in_Stock(stock.quantity - amount)
    
    def __str__(self):
        return self.name