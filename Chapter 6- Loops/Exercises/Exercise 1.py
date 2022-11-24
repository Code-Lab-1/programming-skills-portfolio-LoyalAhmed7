print("what topping would you like on your pizza?")
print("enter 'quit' when you are finished: ")

while True:
    topping = input()
    if topping != 'quit':
        print("I will add " + topping + " to your pizza.")
    else:
        break