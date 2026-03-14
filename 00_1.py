# du z 10.03.2026_Vytvorte program v Pythone, ktorý simuluje bankový účet a
# viacerých klientov pristupujúcich k nemu súčasne pomocou threadov.

# verzia_1: Spustite program bez synchronizácie a sledujte, či je výsledný zostatok správny.

import threading
import time
import random

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
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