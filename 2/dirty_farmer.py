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

class DirtyFarmer(AFarmer):
    def __init__(self, id, source_basket: Basket = None, destiny_basket: Basket = None) -> None:
        super().__init__(id, source_basket, destiny_basket)
        self.is_job_done=False

    
    def get_fruit(self):
        """Get Fruits from Tree
        """
        while self.source_basket.is_empty() == False:
            print(f"Farmer {self.id} getting fruit from {self.source_basket.id}.")
            self.source_basket.get_fruit()
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
            self.put_fruit()
        # TODO notify is done
        self.is_job_done=True

    def put_fruit(self):
        """Put fruits on Dirty Basket
        """
        print(f"Farmer {self.id} putting fruit on {self.destiny_basket.id}.")
        self.destiny_basket.put_fruit()

    def start_job(self):
        pass