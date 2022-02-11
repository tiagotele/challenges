from tree import Tree
from basket import Basket
from abstract_farmer import AFarmer

from tree import Tree
from dirty_basket import Basket
import random
import time

MAX_RANGE=4
MIN_RANGE=2

class CleanFarmer(AFarmer):
    def __init__(self, id, dirty_farmer, source_basket: Basket = None, destiny_basket: Basket = None) -> None:
        super().__init__(id, source_basket, destiny_basket)
        self.dirty_farmer=dirty_farmer
        self.amount=0

    
    def get_fruit(self):
        """Get Fruits from Dirty Basket
        """
        while True:
            self.amount=self.source_basket.get_fruit()
            self.put_fruit(self.amount)
            if self._are_dirty_farmer_working() == False:
                break
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
        

    def put_fruit(self, amount):
        """Put fruits on Clean Basket
        """
        self.destiny_basket.put_fruit(amount)

    def _are_dirty_farmer_working(self):
        for e in self.dirty_farmer:       
            if e.is_job_finisehd == False:
                return True
        return False

    def status(self):
        return f"Cleaner{(self.id+1)} ({self.amount})"