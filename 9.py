import time
import random
from threading import Thread, Lock

class VegetableMarket:
    def __init__(self, capacity):
        self.capacity = capacity
        self.vegetables_in_market = []
        self.market_lock = Lock()

    def add_vegetable(self, vegetable):
        with self.market_lock:
            if len(self.vegetables_in_market) < self.capacity:
                self.vegetables_in_market.append(vegetable)
                print(f"{vegetable} added to the market.")
            else:
                print(f"Market is full. {vegetable} cannot be added.")

    def sell_vegetable(self, vegetable):
        with self.market_lock:
            if vegetable in self.vegetables_in_market:
                self.vegetables_in_market.remove(vegetable)
                print(f"{vegetable} sold to a consumer.")
                return True
            else:
                print(f"{vegetable} not available. Consumer needs to wait.")
                return False

class Farmer(Thread):
    def __init__(self, name, market, vegetables):
        super().__init__()
        self.name = name
        self.market = market
        self.vegetables = vegetables

    def run(self):
        for vegetable in self.vegetables:
            time.sleep(random.uniform(0.5, 1.5))  # Simulating time to produce vegetable
            self.market.add_vegetable(vegetable)

class Consumer(Thread):
    def __init__(self, name, market, desired_vegetable):
        super().__init__()
        self.name = name
        self.market = market
        self.desired_vegetable = desired_vegetable

    def run(self):
        while True:
            time.sleep(random.uniform(1, 3))  # Simulating time between consumer attempts
            if self.market.sell_vegetable(self.desired_vegetable):
                print(f"{self.name} bought {self.desired_vegetable}.")
                break

if __name__ == "__main__":
    market = VegetableMarket(capacity=5)

    farmer1 = Farmer(name="Farmer 1", market=market, vegetables=["Carrot", "Tomato", "Lettuce"])
    farmer2 = Farmer(name="Farmer 2", market=market, vegetables=["Cucumber", "Spinach", "Onion"])

    consumer1 = Consumer(name="Consumer 1", market=market, desired_vegetable="Tomato")
    consumer2 = Consumer(name="Consumer 2", market=market, desired_vegetable="Cucumber")

    farmer1.start()
    farmer2.start()
    consumer1.start()
    consumer2.start()

    farmer1.join()
    farmer2.join()
    consumer1.join()
    consumer2.join()
