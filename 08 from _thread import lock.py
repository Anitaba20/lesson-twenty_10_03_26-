import threading
import time
from _thread import lock
from concurrent.futures import ThreadPoolExecutor


lock = threading.Lock()

class ShoppingCart:
    def __init__(self):
        self.customers_total = 0

    def update(self, name):
        print(f'Zakaznik-{name}: zacina nakupovat')
        lock.acquire()
        total = self.customers_total
        total = total + 1
        time.sleep(1)
        self.customers_total = total
        lock.release()
        print(f'Zakaznik-{name}: nakupil')


print("Nakupovanie zacina")
shopping_cart = ShoppingCart()
print("Pocet zakaznikov:" + str(shopping_cart.customers_total))

zakaznici = ["Patrik", "Anton", "Maryia", "Tomas"]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    for zakaznik in zakaznici:
        futures.append(executor.submit(shopping_cart.update, zakaznik,))
    for future in futures:
        future.result()




# for zakaznik in zakaznici:
#     thread = threading.Thread(target=shopping_cart.update, args=(zakaznik,))
#     thread.start()
#     vlakna.append(thread)
#
# for vlakno in vlakna:
#     vlakno.join()

print("Pocet zakaznikov:" + str(shopping_cart.customers_total))