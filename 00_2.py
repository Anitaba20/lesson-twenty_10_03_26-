# du z 10.03.2026_Vytvorte program v Pythone, ktorý simuluje bankový účet a
# viacerých klientov pristupujúcich k nemu súčasne pomocou threadov.

# verzia_2: Následne program opravte pomocou threading.Lock, aby bol výsledok vždy správny.

import threading
import time
import random

lock = threading.Lock()

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        lock.acquire()

        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.0001)
            self.balance = new_balance

        lock.release()

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
