# Multiprocessing - A module for running multiple processes in parallel on different cpu cores.
#                 - better for cpu bound tasks, ex - video processing, machine learning, etc.

import time
from multiprocessing import Process # importing the Process class from the multiprocessing module
from multiprocessing import cpu_count # importing the cpu_count function from the multiprocessing module

def counter (num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())
    # returns the number of cpu cores in your computer, if your processes are more than the number of cores,
    # the elapsed time will be longer than if the processes are less than the number of cores

    start_time = time.perf_counter()
    a = Process(target=counter, args =(250000000,))
    a.start()
    b = Process(target=counter, args =(250000000,))
    b.start()
    c = Process(target=counter, args =(250000000,))
    c.start()
    d = Process(target=counter, args =(250000000,))
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("finished in:", elapsed_time,  "seconds")

if __name__ == "__main__":
    main()