import threading
import time
import random

class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                time.sleep(0.0001)
                self.balance = new_balance


account = BankAccount(5000)

threads = []

for i in range(10):
    amount = random.randint(1, 10)
    thread = threading.Thread(target=account.withdraw, args=(amount,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Konečný zostatok:", account.balance)