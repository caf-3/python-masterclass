name = "Bianca" # Global scope variable

def sayHello():
    name = "Júlia" # Local scope variable
    print(f'Local {name}')

sayHello()

print(f'Global {name}')