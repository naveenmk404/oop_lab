import threading
import time

# Global variable for synchronization
counter = 1
lock = threading.Lock()

# Function to print numbers from 1 to 5
def function_A():
    global counter
    for i in range(5):
        with lock:
            while counter % 2 != 1:  # Wait if it's not the turn for numbers
                lock.release()
                time.sleep(0.1)
                lock.acquire()
            print(i + 1)
            counter += 1
            time.sleep(0.1)  # Simulating a time-consuming task

# Function to print letters 'A' to 'E'
def function_B():
    global counter
    for char in 'ABCDE':
        with lock:
            while counter % 2 != 0:  # Wait if it's not the turn for letters
                lock.release()
                time.sleep(0.1)
                lock.acquire()
            print(char)
            counter += 1
            time.sleep(0.1)  # Simulating a time-consuming task

def main():
    # Create two threads, one for function_A and one for function_B
    thread_A = threading.Thread(target=function_A)
    thread_B = threading.Thread(target=function_B)

    # Start both threads
    thread_A.start()
    thread_B.start()

    # Wait for both threads to complete
    thread_A.join()
    thread_B.join()

if __name__ == "__main__":
    main()
