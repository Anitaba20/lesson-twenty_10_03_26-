import threading
import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor


def download_site(i):
    time.sleep(3)
    print("Stiahnutie: " + str(i))

start_time = time.time()

threads = []
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = []
    for i in range(4000):
        futures.append(executor.submit(download_site, i))

    for future in futures:
        result = future.result()
        print(result)


duration = time.time() - start_time
print(f"Trvanie {duration} sekúnd")