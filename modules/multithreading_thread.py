import threading
import time

# thread = a flow of execution. Like a separate order of instructions. However each threades takes a turn running to achieve concurrency
# GIL - Global Interpreter Lock, allows only one thread to execute at a time in CPython
# meaning multithread will take turns to run


# cpu bound - CPU intensive, doing a lot of computation, better to use multiprocessing
# io bound - program is bottlenecked by I/O, like network, disk, etc. Better to use multithreading


print(threading.active_count()) # returns the number of threads running
print(threading.enumerate()) # returns a list of all the threads running


# These three are iobound tasks
def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finished studying")

# Running one thread at a time
# eat_breakfast()
# drink_coffee()
# study()

# Running all threads at the same time
thread1 = threading.Thread(target=eat_breakfast)
thread1.start()
thread2 = threading.Thread(target=drink_coffee)
thread2.start()
thread3 = threading.Thread(target=study)
thread3.start()

# Joining the threads to make sure they finish before the program ends
thread1.join()
thread2.join()
thread3.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter()) # returns the time in seconds since the process started