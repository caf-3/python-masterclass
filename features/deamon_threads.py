import threading
import time

def timer():
    counter = 0

    while True:
        time.sleep(1)
        counter += 1
        print(f'loggend in for: {counter} seconds')
        print()

counterThread = threading.Thread(target=timer, daemon=True)
counterThread.start()


a = input('type something: ')
print(f'\nIs counterThread a daemon thread ?: {counterThread.isDaemon()}')

print(f'performance: {time.perf_counter()}')