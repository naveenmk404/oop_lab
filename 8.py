import threading
import random
import time

# Shared variable between threads
shared_value = None

# Lock for synchronization
lock = threading.Lock()

# Iteration count
iteration_count = 10  # You can adjust this count as needed

# Function for the first thread to generate random integers
def generate_random_integer():
    global shared_value
    for _ in range(iteration_count):
        with lock:
            shared_value = random.randint(1, 100)
        time.sleep(1)

# Function for the second thread to compute square if the value is even
def compute_square():
    global shared_value
    for _ in range(iteration_count):
        with lock:
            if shared_value is not None and shared_value % 2 == 0:
                print(f"Square: {shared_value ** 2}")
        time.sleep(1)

# Function for the third thread to print cube if the value is odd
def print_cube():
    global shared_value
    for _ in range(iteration_count):
        with lock:
            if shared_value is not None and shared_value % 2 != 0:
                print(f"Cube: {shared_value ** 3}")
        time.sleep(1)

if __name__ == "__main__":
    # Creating threads
    thread1 = threading.Thread(target=generate_random_integer)
    thread2 = threading.Thread(target=compute_square)
    thread3 = threading.Thread(target=print_cube)

    # Starting threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Waiting for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
