import threading

class Basket():
    def __init__(self, fruits: int = 0) -> None:
        self.fruits=fruits
        self._lock=threading.Lock()

    def get_fruit(self):
        if self.fruits > 0:
            with self._lock:
                self.fruits -= 1
    
    def put_fruit(self):
        with self._lock:
            self.fruits += 1

    def is_empty(self):
        return self.fruits == 0
    
