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
    def __init__(self, source_basket: Basket = None, destiny_basket: Basket = None) -> None:
        super().__init__(source_basket, destiny_basket)

    
    def getFruit(self):
        """Get Fruits from Tree
        """
        while self.source_basket.is_empty() == False:
            self.source_basket.get_fruit()
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
            self.putFruit()
        # TODO notify is done

    def putFruit(self):
        """Put fruits on Dirty Basket
        """
        self.destiny_basket.put_fruit()

    def start_job(self):
        pass