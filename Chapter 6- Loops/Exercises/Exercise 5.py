sandwich_orders = ['fish', 'chicken', 'beef', 'grilled chicken', 'pastrami', 'pastrami','pastrami']
finished_sandwiches = []
print("I am sorry, we are all out of pastrami today")                                   
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print("I have just made your " + sandwich + " sandwich.")