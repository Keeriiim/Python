# daemon threads - a thread that runs in the background, not important for program to run
#                  Your program will not wait for daemon threads to complete before exiting
#                  Non-daemon threads cannot normally be killed, stay alive until task is complete
#        examples: - garbage collection, sending a signal, input

import time
import threading

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, " seconds")

# daemon = True ensures that once the program is ran, everything will end.
x = threading.Thread(target=timer) # Add ,daemon=True 

# x.setDaemon() # Sets a non demonthread to a daemonthread while it's running
print(x.__getstate__())

x.start()

answer = input("Do you wish to exit? ")