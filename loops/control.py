import time
# Break = used to terminate the loop entirely
# Continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Input your name: ")
    if name != "":
        print("Terminating the loop...")
        # time.sleep(3)
        break

print()

phone_number = "+258-84-27-48-524"

for i in phone_number:
    if(i == '-'):
        continue
    print(i, end="")

print()
print()

name = input("Input your name: ")

for j in name:
    if(j == 'o' or j == 'O'):
        pass
    else:
        print(j, end="")