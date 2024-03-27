import time_import

#epoch time - time since 1st Jan 1970
print(time.time()) # return current seconds since epoch
print(time.ctime(0)) # return the time in human readable format

print(time.ctime(time.time())) # Todays date and time

time_object = time.localtime()
print(time_object)