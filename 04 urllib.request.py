import threading
import urllib.request
import time

def download_site(url):
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")


sites = [
    "http://www.example.com",
    "http://t3s.dendis.tech/obrazky/mercedes_trip.jpg",
    "http://t3s.dendis.tech/obrazky/family_trip.jpg",
    "https://www.antimon.gov.sk/kaumy-group-as-praha-ceska-republika/?csrt=5446518496088320315",
    "https://www.antimon.gov.sk/ice-industrial-services-as-praha-ceska-republika-hsf-system-as-ostrava-ceska-republika",
    "https://www.antimon.gov.sk/zlaty-bazant-as-hurbanovo-hurbanovo;-stefan-pisak-michalovce/?csrt=5446518496088320315"
]

start_time = time.time()
threads = []
for site in sites:
    thr = threading.Thread(target=download_site, args=(site,))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()

duration = time.time() - start_time
print(f"Stiahnuté {len(sites)} stránok za {duration} sekúnd")