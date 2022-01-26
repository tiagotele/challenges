import threading

class Basket:
    def __init__(self, fruits=0) -> None:
        self.fruits=fruits
        self._lock = threading.Lock()
    
    def put_fruit(self):
        with self._lock:
            self.fruits += 1
            print(f"Basket has {self.fruits} fruits.")
