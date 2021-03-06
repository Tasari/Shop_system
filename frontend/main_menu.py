from tkinter import Tk, Label, Button
from tkinter.ttk import Notebook, Frame
from frontend.order.order_tab import order_tab_menu
from frontend.products.product_tab import products_tab_menu
from frontend.stock.stock_tab import stock_tab_menu
from frontend.workers.workers_tab import workers_tab_menu

def main_menu(wallet, user):
    main_menu = Tk()
    main_menu.title("Main Menu")
    tabs = Notebook(main_menu)
    tabs.grid(column=0, row=0, columnspan=25, rowspan=25, sticky="NEWS")
    
    tab_Order = Frame(tabs)
    order_tab_menu(tab_Order, wallet, user)

    tab_Products = Frame(tabs)
    products_tab_menu(tab_Products)

    tab_Stock = Frame(tabs)
    stock_tab_menu(tab_Stock)

    tab_Workers = Frame(tabs)
    workers_tab_menu(tab_Workers)

    tabs.add(tab_Order, text="Order")
    tabs.add(tab_Products, text="Products")
    tabs.add(tab_Stock, text="Stock")
    tabs.add(tab_Workers, text="Workers")
    main_menu.mainloop()
