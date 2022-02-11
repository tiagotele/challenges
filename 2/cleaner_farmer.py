from tree import Tree
from basket import Basket
from abstract_farmer import AFarmer

from urllib.parse import MAX_CACHE_SIZE
from tree import Tree
from dirty_basket import Basket
import random
import time
import threading

MAX_RANGE=3
MIN_RANGE=1

class CleanFarmer(AFarmer):
    def __init__(self, id, dirty_farmer, source_basket: Basket = None, destiny_basket: Basket = None) -> None:
        super().__init__(id, source_basket, destiny_basket)
        self.dirty_farmer=dirty_farmer

    
    def get_fruit(self):
        """Get Fruits from Dirty Basket
        """
        while True:
            print(f"Cleaner {self.id} getting fruit from {self.source_basket.id}.")
            amount=self.source_basket.get_fruit()
            self.put_fruit(amount)
            if self._are_dirty_farmer_working() == False:
                break
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
        

    def put_fruit(self, amount):
        """Put fruits on Clean Basket
        """
        print(f"Cleaner {self.id} putting fruit on {self.destiny_basket.id}.")
        self.destiny_basket.put_fruit(amount)
        #TODO check if dirty farmers has finished their jobs

    def _are_dirty_farmer_working(self):
        for e in self.dirty_farmer:       
            if e.is_job_finisehd == False:
                return True
        return False

    def start_job(self):
        pass