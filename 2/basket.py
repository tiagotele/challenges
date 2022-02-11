import threading

class Basket():
    def __init__(self, id: str, fruits: int = 0) -> None:
        self.id=id
        self.fruits=fruits
        self._lock=threading.Lock()

    def get_fruit(self):
        with self._lock:
            if self.fruits > 0:
                self.fruits -= 1
                return 1
            return 0
    
    def put_fruit(self, amount):
        with self._lock:
            self.fruits += amount

    def is_empty(self):
        with self._lock:
            return self.fruits == 0
    
    def status(self):
        return f"{self.id} ({self.fruits})"
    
