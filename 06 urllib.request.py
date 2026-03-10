import threading
import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor


def download_site(url):
    with urllib.request.urlopen(url) as response:
        return f"Stiahnutie {url}: {len(response.read())} bytov"


sites = [
    "http://www.example.com",
    "http://t3s.dendis.tech/obrazky/mercedes_trip.jpg",
    "http://t3s.dendis.tech/obrazky/family_trip.jpg",
    "https://www.antimon.gov.sk/kaumy-group-as-praha-ceska-republika/?csrt=5446518496088320315",
    "https://www.antimon.gov.sk/ice-industrial-services-as-praha-ceska-republika-hsf-system-as-ostrava-ceska-republika",
    "https://www.antimon.gov.sk/zlaty-bazant-as-hurbanovo-hurbanovo;-stefan-pisak-michalovce/?csrt=5446518496088320315"
]

start_time = time.time()
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = []
    for site in sites:
        futures.append(executor.submit(download_site, site))

    for future in futures:
        result = future.result()
        print(result)

duration = time.time() - start_time
print(f"Stiahnuté {len(sites)} stránok za {duration} sekúnd")