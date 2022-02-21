def greetings(name, age):
    if(age >= 18):
        print(f"Your are welcome {name} for joining our service")
    else:
        print(f'Dear {name}, to subscribe to our service, you need more {18 - age} years!')

greetings('Tomás Caetano', 21);