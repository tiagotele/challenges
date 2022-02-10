from basket import Basket

from abc import ABC, abstractmethod
from urllib.parse import MAX_CACHE_SIZE
import random
import time

MAX_RANGE=3
MIN_RANGE=1


class AFarmer(ABC):
    def __init__(self, id:int, source_basket: Basket = None, destiny_basket: Basket = None) -> None:
        self.id=id
        self.source_basket=source_basket
        self.destiny_basket=destiny_basket

    @abstractmethod
    def get_fruit(self):
        pass

    @abstractmethod
    def put_fruit(self):
        pass

    @abstractmethod
    def start_job(self):
        pass