print("how old are you?")
print("enter 'quit' when you are done")

while True:
    age = input()
    if age == 'quit':
        break
    age=int(age)

    if age < 3:
        print("""You get in free!
        """)
    elif age < 13:
        print("""Your ticket is $10
        """)
    else:
        print("""Your ticket is $15
        """)