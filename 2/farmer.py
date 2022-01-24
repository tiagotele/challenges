from tree import Tree
import random
import time

class Farmer:
    def __init__(self, id: int, tree: Tree) -> None:
        self.id=id
        self.tree=tree
    
    def get_fruit(self):
        while self.tree.is_empty() == False:
            print(f"farmer {self.id} getting fruit")
            self.tree.get_fruit()
            time_to_collect=random.randint(3, 6)
            time.sleep(time_to_collect)
            self._put_fruit_on_basket()
            print(f"farmer {self.id} putting on basket")
        print(f"farmer {self.id} end job")

    def _put_fruit_on_basket(self):
        pass