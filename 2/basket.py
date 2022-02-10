import threading

class Basket():
    def __init__(self, id: str, fruits: int = 0) -> None:
        self.id=id
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
        print(f"{self.id} remaining {self.fruits} fruits.")
        return self.fruits == 0
    
    def status(self):
        return f"{self.id} has {self.fruits}."
    
