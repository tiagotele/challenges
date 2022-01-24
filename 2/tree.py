import threading


class Tree:
    def __init__(self, fruits=50) -> None:
        self.fruits=fruits
        self._lock = threading.Lock()
    
    def get_fruit(self):
        if self.fruits >= 0:
            with self._lock:
                self.fruits -= 1
        else:
            #TODO
            pass
