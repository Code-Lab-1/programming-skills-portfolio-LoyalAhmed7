sandwich_orders = ['fish', 'chicken', 'beef', 'grilled chicken']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()                                                      
    print("I am working on your " + current_sandwich + " sandwich.")                               
    finished_sandwiches.append(current_sandwich)                                                  
for sandwich in finished_sandwiches:
    print("I have just made your " + sandwich + " sandwich.")