# **kwargs = parameter that will pack all arguments into a dictornary
#            uuseful so that a function can accept a varying amount of keyword arguments

def sayHello(**kwargs):

    # return f"{kwargs['firstName']} {kwargs['lastName']} Your mom ({kwargs['montherName']}) loves you so much!"
    for key, value in kwargs.items():
        print(f' {key} -> {value}', end=' ')

sayHello(lastName='Caetano', montherName='Celia', firstName='Tomás')