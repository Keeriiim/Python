

try:
    print(1/0)
except Exception as e:
    print("An error occurred! : " + str(e))

else:
    print("No exception occurred")
finally:
    print("This will always run")
