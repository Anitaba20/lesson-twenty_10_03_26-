import threading
import time
import queue

buffer = queue.Queue(maxsize=10)

def producer():
    for i in range(50):
        item = f"item {i}"
        buffer.put(item)
        print(f"Produced {item}")
        time.sleep(0.01)
    print("Producer finished.")

def consumer():
    while True:
        item = buffer.get()
        if item is None:
            break
        print(f"Consumed {item}")
        time.sleep(2)
    print("Consumer finished.")


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
buffer.put(None)
consumer_thread.join()