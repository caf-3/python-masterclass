
try:
    with open('files/text.txxt') as file:
        print(file.read())

    print(file.closed)
except FileNotFoundError:
    print("File not found 404 :(")