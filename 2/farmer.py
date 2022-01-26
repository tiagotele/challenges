from urllib.parse import MAX_CACHE_SIZE
from tree import Tree
from dirty_basket import Basket
import random
import time

MAX_RANGE=3
MIN_RANGE=1
class Farmer:
    def __init__(self, id: int, tree: Tree, dirty_basket: Basket, clean_basket: Basket) -> None:
        self.id=id
        self.tree=tree
        self.dirty_basket = dirty_basket
        self.clean_basket = clean_basket
    
    def get_fruit_from_tree(self):
        while self.tree.is_empty() == False:
            print(f"farmer {self.id} getting fruit from tree")
            self.tree.get_fruit()
            time_to_collect=random.randint(MIN_RANGE, MAX_RANGE)
            time.sleep(time_to_collect)
            self._put_fruit_on_dirty_basket()
            print(f"farmer {self.id} putting on dirty basket")
        self.dirty_basket.will_have_more_fruits=False
        print(f"farmer {self.id} end job")
    
    def _put_fruit_on_dirty_basket(self):
        self.dirty_basket.put_fruit()

    def get_fruit_from_dirty_basket(self):
        while self.clean_basket.will_have_more_fruits == True:
            print(f"cleaner {self.id} getting fruit from dirty basket")
            self.dirty_basket.get_fruit()
            time_to_collect=random.randint(MIN_RANGE, MAX_CACHE_SIZE)
            time.sleep(time_to_collect)
            self._put_fruit_on_clean_basket()
            print(f"cleaner {self.id} putting on clean basket")
        print(f"cleaner {self.id} end job")

    def _put_fruit_on_clean_basket(self):
        self.clean_basket.put_fruit()