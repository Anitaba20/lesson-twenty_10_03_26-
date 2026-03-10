import threading
import time

file_lock = threading.Lock()

def load_numbers(path):
    cisla = []
    with open(path, 'r') as file:
        for line in file:
            cisla_string = line.strip().split(sep=",")
            for cislo in cisla_string:
                cisla.append(int(cislo))
    return cisla

def write_numbers(path, numbers, is_even):
    with open(path, 'a') as file:
        cisla = []
        time.sleep(5)
        for number in numbers:
            if number % 2 == 0 and is_even:
                cisla.append(str(number))
            elif number % 2 != 0 and not is_even:
                cisla.append(str(number))
        parne_cisla_string = ",".join(cisla) + ","
        file_lock.acquire()
        file.write(parne_cisla_string)
        file_lock.release()

cisla_zo_suboru = load_numbers("cisla.txt")

start_time = time.time()
parne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru,True,))
neparne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru,False))

parne.start()
neparne.start()

neparne.join()
parne.join()

duration = time.time() - start_time
print(f"Dokoncene za {duration} sekúnd")