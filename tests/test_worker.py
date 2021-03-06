from tables.worker import Worker
from tables.order import Order
from unittest.mock import MagicMock
from tools import string_to_object_from_table
def test_worker_creation():
    '''
    Tests valid creation of object from table
    '''
    worker = Worker("toBias HayMond", 'thaymond', 'tobiash')
    assert worker.name == 'Tobias Haymond'
    assert worker.rank == 0
    assert worker.orders == []
    assert worker.work_hours == 0
    assert worker.username == 'thaymond'
    assert worker.password == 'tobiash'

def test_worker_promotion():
    '''
    Tests promotion and demotion of worker
    '''
    worker = string_to_object_from_table('Jack Smith', Worker)
    worker.promotion()
    assert worker.rank == 1
    worker.promotion()
    assert worker.rank == 2
    worker.promotion(-2)
    assert worker.rank == 0

def test_worker_work_hours():
    '''
    Tests adding work hours to worker data
    '''
    worker = string_to_object_from_table('Jack Smith', Worker)
    worker.add_work_hours(15)
    assert worker.work_hours == 15
    worker.add_work_hours(5)
    assert worker.work_hours == 20

def test_worker_finish_order():
    '''
    Tests valid adding order to ones finished by worker
    '''
    worker = string_to_object_from_table('Jack Smith', Worker)
    order = Order()
    order.add_product_to_order('Hamburger', 2)
    worker.finish_order(MagicMock(), order)
    assert order in worker.orders

def test_worker_orders_price():
    '''
    Tests valid counting of money from orders created by worker
    '''
    worker = string_to_object_from_table('Paul Phoenix', Worker)
    worker.orders = []
    order = Order()
    order.add_product_to_order('hamburger', 2)
    worker.finish_order(MagicMock(), order)
    order = Order()
    order.add_product_to_order('hamburger', 1)
    order.add_product_to_order('french fries', 1)
    worker.finish_order(MagicMock(), order)
    assert worker.orders_price_sum() == 6.4
    