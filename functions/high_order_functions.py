# A function that either:
# 1. accepts a function as an argument
#   or
# 2. returns a function
# (In python, functions are also treated as object)


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func('Bom dia.')
    print(text)

hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(30))