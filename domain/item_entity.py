import datetime
from tokenize import String
from xmlrpc.client import DateTime

from sqlalchemy import Column, Integer, Float

import database
from database import Base as Base


class ItemEntity:
    # __tablename__ = 'item'

    def __init__(self, name: str, price: int, description: str, tax: float = None):
        self.item_id = None
        self.name = name
        self.price = price
        self.description = description
        self.tax = tax
        self.create_time = datetime.datetime.now()
        self.update_time = None

    # item_id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String, nullable=False)
    # price = Column(Integer, nullable=False)
    # description = Column(String)
    # tax = Column(Float)
    # create_time = Column(DateTime, default=datetime.datetime.now)
    # update_time = Column(DateTime)

    # toString
    def __str__(self):
        return f'name = {self.name},\n price = {self.price},\n description = {self.description},\n create_time = {self.create_time}'

    def set_item_id(self, item_id: int):
        self.item_id = item_id

    def set_tax(self):
        self.tax = self.price * 0.1

    def set_update_time(self):
        self.update_time = datetime.datetime.now()

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_item_id(self):
        return self.item_id

    def get_price(self):
        return self.price

    def change_name(self, new_name: str):
        self.name = new_name

    def change_price(self, new_price: int):
        self.price = new_price

    def change_description(self, new_description: str):
        self.description = new_description

    def get_tax(self):
        return self.tax

    def get_create_time(self):
        return self.create_time

    def get_update_time(self):
        return self.update_time
