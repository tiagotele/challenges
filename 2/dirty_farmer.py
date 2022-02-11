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

    
    def get_fruit(self):
        """Get Fruits from Tree
        """
        while True:
            print(f"Farmer {self.id} getting fruit from {self.source_basket.id}.")
            amount=self.source_basket.get_fruit()
            self.put_fruit(amount)
            if self.source_basket.is_empty() == True:
                break
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
        # TODO notify is done
        self.is_job_finisehd=True

    def put_fruit(self, amount):
        """Put fruits on Dirty Basket
        """
        print(f"Farmer {self.id} putting fruit on {self.destiny_basket.id}.")
        self.destiny_basket.put_fruit(amount)

    def start_job(self):
        pass