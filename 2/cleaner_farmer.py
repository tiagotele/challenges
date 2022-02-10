from tree import Tree
from basket import Basket
from abstract_farmer import AFarmer

from urllib.parse import MAX_CACHE_SIZE
from tree import Tree
from dirty_basket import Basket
import random
import time

MAX_RANGE=3
MIN_RANGE=1

class CleanFarmer(AFarmer):
    def __init__(self, id, source_basket: Basket = None, destiny_basket: Basket = None) -> None:
        super().__init__(id, source_basket, destiny_basket)

    
    def get_fruit(self):
        """Get Fruits from Dirty Basket
        """
        while True:
            print(f"Cleaner {self.id} getting fruit from {self.source_basket.id}.")
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
            if self.source_basket.get_fruit() == 0:
                print(f"{self.source_basket.id} is  zero = {self.source_basket.get_fruit()}")
                continue
            else:
                print(f"{self.source_basket.id} is not zero = {self.source_basket.get_fruit()}")
            self.put_fruit()
            self.source_basket.is_empty()
            self.destiny_basket.is_empty()

    def put_fruit(self):
        """Put fruits on Clean Basket
        """
        print(f"Cleaner {self.id} putting fruit on {self.destiny_basket.id}.")
        self.destiny_basket.put_fruit()
        #TODO check if dirty farmers has finished their jobs

    def start_job(self):
        pass