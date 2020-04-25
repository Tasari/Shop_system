from tables.stock import Stock, update_object_quantity_in_Stock
from wallet import Wallet
from tools import string_to_object_from_table

def test_stock_creation():
    '''
    Tests valid creation of object from table
    '''
    stock = Stock('eggs', 0.5)
    assert stock.name == 'Eggs'
    assert stock.quantity == 0
    assert stock.restock_price == 0.5

def test_restock_add():
    '''
    Tests adding item's amount to stock
    '''
    stock_old = string_to_object_from_table('hAm',Stock)
    stock_old.restock(15, Wallet(99999))
    stock_new = string_to_object_from_table('hAm',Stock)
    assert stock_old.quantity+15 == stock_new.quantity
    stock_new.restock(15, Wallet(99999))
    assert stock_new.quantity + 15 == string_to_object_from_table('hAm',Stock).quantity

def test_restock_set():
    '''
    Tests setting item's amount to stock
    '''
    stock = string_to_object_from_table("SpAm", Stock)
    stock.restock(15, Wallet(99999), mode='set')
    assert 15 == string_to_object_from_table("SpAm", Stock).quantity
    stock = string_to_object_from_table('sPAm', Stock)
    stock.restock(15, Wallet(99999), mode='set')
    assert stock.quantity == 15
    assert stock.quantity != 30

def test_restock_add_wallet():
    '''
    Tests subtracting cost of item from wallet
    '''
    stock = Stock('ham', 1)
    wallet = Wallet(50)
    stock.restock(15, wallet)
    assert wallet.money == 35
    stock.restock(15, wallet)
    assert wallet.money == 20

def test_restock_set_wallet():
    '''
    Tests setting wallet money based on previous money in it
    '''
    update_object_quantity_in_Stock('SpAm', 0)
    stock = string_to_object_from_table('SPaM', Stock)
    wallet = Wallet(250)
    stock.restock(15, wallet, mode='set')
    assert wallet.money == 25
    stock = string_to_object_from_table('SPaM', Stock)
    stock.restock(15, wallet, mode='set')
    assert wallet.money == 25
    stock = string_to_object_from_table('SPaM', Stock)
    stock.restock(10, wallet, mode='set')
    assert wallet.money == 100

def test_update_item_in_stock():
    '''
    Tests valid substraction of item's amount from quantity in stock
    '''
    update_object_quantity_in_Stock('haM', 30)
    stock = string_to_object_from_table('Ham', Stock)
    assert stock.quantity == 30
    update_object_quantity_in_Stock(stock.name, stock.quantity-2)
    stock = string_to_object_from_table('Ham', Stock)
    assert string_to_object_from_table('Ham', Stock).quantity == 28
    update_object_quantity_in_Stock(stock.name, stock.quantity+2)
    stock = string_to_object_from_table('Ham', Stock)
    assert string_to_object_from_table('Ham', Stock).quantity == 30    