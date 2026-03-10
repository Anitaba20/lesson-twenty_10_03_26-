# import threading
#
# def load_numbers(path):
#     cisla = []
#     with open(path, 'a') as file:
#         for line in file:
#             cisla_string = line.strip().split(sep=",")
#             for cislo in cisla_string:
#                 cisla.append(int(cislo))
#     return cisla
#
#
# def write_numbers(path, numbers, is_even):
#     with open(path, 'w') as file:
#         cisla = []
#         for number in numbers:
#             if number % 2 == 0 and is_even:
#                 cisla.append(str(number))
#             elif number % 2 != 0 and not is_even:
#                 cisla.append(str(number))
#         parne_cisla_string = ",".join(cisla)
#         file.write(parne_cisla_string)
#
#
# cisla_zo_suboru = load_numbers("cisla.txt")
#
# write_numbers("cisla_nove.txt", cisla_zo_suboru, False)
#
# parne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru, True,))
# neparne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru, False))
#
# parne.start()
# neparne.start()
#
# parne.join()
# neparne.join()
#
# print("Dokoncene")

# import threading
#
# lock = threading.Lock()
#
#
# def load_numbers(path):
#     cisla = []
#     with open(path, 'r') as file:
#         for line in file:
#             cisla_string = line.strip().split(sep=",")
#             for cislo in cisla_string:
#                 cisla.append(int(cislo))
#     return cisla
#
#
# def write_numbers(path, numbers, is_even):
#     with lock:
#         with open(path, 'w') as file:
#             cisla = []
#             for number in numbers:
#                 if number % 2 == 0 and is_even:
#                     cisla.append(str(number))
#                 elif number % 2 != 0 and not is_even:
#                     cisla.append(str(number))
#             parne_cisla_string = ",".join(cisla)
#             file.write(parne_cisla_string)
#
#
# cisla_zo_suboru = load_numbers("cisla.txt")
#
# parne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru, True))
# neparne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru, False))
#
# parne.start()
# neparne.start()
#
# parne.join()
# neparne.join()
#
# print("Dokoncene")

import threading

lock = threading.Lock()

def load_numbers(path):
    cisla = []
    with open(path, 'r') as file:
        for line in file:
            cisla_string = line.strip().split(",")
            for cislo in cisla_string:
                if cislo != "":
                    cisla.append(int(cislo))
    return cisla


def write_numbers(path, numbers, is_even):
    cisla = []
    for number in numbers:
        if number % 2 == 0 and is_even:
            cisla.append(str(number))
        elif number % 2 != 0 and not is_even:
            cisla.append(str(number))

    text = ",".join(cisla)

    with lock:
        with open(path, 'a') as file:
            if file.tell() > 0 and text:
                file.write("," + text)
            else:
                file.write(text)


cisla_zo_suboru = load_numbers("cisla.txt")

# vymazanie starého obsahu súboru
with open("cisla_nove.txt", "w") as file:
    pass

parne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru, True))
neparne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru, False))

parne.start()
neparne.start()

parne.join()
neparne.join()

print("Dokoncene")