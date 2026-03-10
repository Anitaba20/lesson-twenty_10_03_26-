# Task 3
# The user types in a path to a file containing a set of numbers.
# After that, two threads start. The first thread creates a new file where it writes only
# even elements from the list. The second thread creates a new file where it writes only odd elements from the list
# Print the number of even and odd elements.
#
# Úloha 3
# Používateľ zadá cestu k súboru obsahujúcemu množinu čísel. Potom sa spustia dve vlákna.
# Prvé vlákno vytvorí nový súbor, do ktorého zapíše iba párne prvky zo zoznamu.
# Druhé vlákno vytvorí nový súbor, do ktorého zapíše iba nepárne prvky zo zoznamu.
# Vypíšte počet párnych a nepárnych prvkov.
# 10_03_2026



# import threading
#
# cisla = [1, 2, 3, 4]
#
# def parne():
#     for n in cisla:
#         if n % 2 == 0:
#             print("Párne:", n)
#
# def neparne():
#     for n in cisla:
#         if n % 2 != 0:
#             print("Nepárne:", n)
#
# t1 = threading.Thread(target=parne)
# t2 = threading.Thread(target=neparne)
#
# t1.start()
# t2.start()

# cisla = list(map(int, open("cisla.txt").read().split()))
#
# def parne():
#     c = 0
#     with open("parne.txt","w") as f:
#         for n in cisla:
#             if n % 2 == 0:
#                 f.write(str(n)+"\n"); c += 1
#     print("Párne:", c)
#
# def neparne():
#     c = 0
#     with open("neparne.txt","w") as f:
#         for n in cisla:
#             if n % 2 != 0:
#                 f.write(str(n)+"\n"); c += 1
#     print("Nepárne:", c)
#
# threading.Thread(target=parne).start()
# threading.Thread(target=neparne).start()
#
# import threading
# import os
#
# if not os.path.exists("cisla.txt"):
#     f = open("cisla.txt", "w")
#     f.write("1 2 3 4 5 6")
#     f.close()
#
# cisla = list(map(int, open("cisla.txt").read().split()))
#
# def parne():
#     c = 0
#     with open("parne.txt", "w") as f:
#         for n in cisla:
#             if n % 2 == 0:
#                 f.write(str(n) + "\n")
#                 c += 1
#     print("Párne:", c)
#
# def neparne():
#     c = 0
#     with open("neparne.txt", "w") as f:
#         for n in cisla:
#             if n % 2 != 0:
#                 f.write(str(n) + "\n")
#                 c += 1
#     print("Nepárne:", c)
#
# threading.Thread(target=parne).start()
# threading.Thread(target=neparne).start()

import threading
path = input("Zadaj cestu k súboru: ")
cisla = list(map(int, open(path).read().split()))

def parne():
    pocet = 0
    with open("parne.txt", "w") as f:
        for n in cisla:
            if n % 2 == 0:
                f.write(str(n) + "\n")
                pocet += 1
    print("Počet párnych:", pocet)

def neparne():
    pocet = 0
    with open("neparne.txt", "w") as f:
        for n in cisla:
            if n % 2 != 0:
                f.write(str(n) + "\n")
                pocet += 1
    print("Počet nepárnych:", pocet)

t1 = threading.Thread(target=parne)
t2 = threading.Thread(target=neparne)

t1.start()
t2.start()