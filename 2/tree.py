import threading
import random
import time

class Tree:
    def __init__(self, fruits=50) -> None:
        self.fruits=fruits
        self._lock = threading.Lock()
    
    def get_fruit(self):
        if self.fruits >= 0:
            with self._lock:
                time_to_collect=random.randint(0, 9)
                time.sleep(time_to_collect)
                self.fruits -= 1
        else:
            #TODO
            pass
