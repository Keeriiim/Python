# 1. Accepts a function as an argument or
# 2. Returns a function (functions are objects in Python)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend

# divide is a function that takes an argument and divides it by 2
divide = divisor(2)

# Sending 10 to divide will return 5.0
print(divide(10)) #5.0