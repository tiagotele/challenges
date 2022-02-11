from tree import Tree
from basket import Basket
from abstract_farmer import AFarmer

from tree import Tree
from dirty_basket import Basket
import random
import time

MAX_RANGE=6
MIN_RANGE=3

class DirtyFarmer(AFarmer):
    def __init__(self, id, source_basket: Basket = None, destiny_basket: Basket = None) -> None:
        super().__init__(id, source_basket, destiny_basket)
        self.amount=0

    
    def get_fruit(self):
        """Get Fruits from Tree
        """
        while True:
            self.amount=self.source_basket.get_fruit()
            self.put_fruit(self.amount)
            if self.source_basket.is_empty() == True:
                break
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
        self.is_job_finisehd=True

    def put_fruit(self, amount):
        """Put fruits on Dirty Basket
        """
        self.destiny_basket.put_fruit(amount)

    def status(self):
        return f"Farmer{(self.id+1)} ({self.amount})"