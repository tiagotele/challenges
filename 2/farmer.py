from tree import Tree
import random
import time

class Farmer:
    def __init__(self, id: int, tree: Tree) -> None:
        self.id=id
        self.tree=tree
    
    def get_fruit(self):
        print(f"farmer {self.id} getting fruit")
        time_to_collect=random.randint(0, 2)
        time.sleep(time_to_collect)
        # self.tree.get_fruit()
        self._put_fruit_on_basket()
        print(f"farmer {self.id} putting on basket")

    def _put_fruit_on_basket(self):
        pass