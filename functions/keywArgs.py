def sayHello(firstName: str, secondName: str, lastName: str) -> str:
    return f'Hello {firstName} {secondName} {lastName}'

helloMessage = sayHello(lastName="Matsolo", secondName="Caetano", firstName="Tomás")

print(helloMessage)