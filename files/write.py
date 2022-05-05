def writeToAFile(mode:str) -> None:
    content = input("Write down the file content:\n")
    with open('files/write.txt', mode) as file:
        file.write(content)

try:
    cond = input("Do you want to write or append new text ?\nW - Write\nA - Append\nAnswer:")
    while cond.lower() != 'a' and cond.lower() != 'w':
        cond = input("Do you want to write or append new text ?\nW - Write\nA - Append\nE, 0 or exit - Exit\nAnswer:")
        if cond.lower() != '0' and cond.lower() != 'e' and cond.lower() != 'exit':
            writeToAFile(cond)
        else:
            print('Exiting program...')
            break
    writeToAFile(cond)
    
except Exception as e:
    print(e)