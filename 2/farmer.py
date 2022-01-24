from tree import Tree


class Farmer:
    def __init__(self, id: int, tree: Tree) -> None:
        self.id
        self.tree=tree
    
    def get_fruit(self):
        self.tree.get_fruit()
        self._put_fruit_on_basket()

    def _put_fruit_on_basket(self):
        pass