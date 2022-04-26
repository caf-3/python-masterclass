try:
    numerator = int(input("Insert the numerator: "))
    denominator = int(input("Insert the denominator: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print('You must insert only numbers!')
except Exception as e:
    print(e)
    print("Something went wrong :/")
else: 
    print(result)
finally:
    print("Program ending execution...")