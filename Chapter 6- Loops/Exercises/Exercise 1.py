print("what topping would you like to have on your pizza?")
print("enter 'quit' when you are done: ")

while True:
    topping = input()
    if topping != 'quit':
        print("I will add " + topping + " to your pizza.")
    else:
        break