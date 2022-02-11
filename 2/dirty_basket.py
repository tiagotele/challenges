import threading

class Basket:
    def __init__(self, fruits=0, name='') -> None:
        self.fruits=fruits
        self._lock = threading.Lock()
        self.name=name
    
    def put_fruit(self):
        with self._lock:
            self.fruits += 1
            print(f"Basket {self.name} has {self.fruits} fruits.")
    
    def get_fruit(self):
        if self.fruits > 0:
            with self._lock:
                self.fruits -= 1
    
