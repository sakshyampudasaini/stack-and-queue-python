# Stack Program in Python
# Author: sakshyampudasaini

l = []
while True:
    c = int(input('''
        1. Push Element
        2. Pop Element
        3. Peek Element
        4. Display Stack
        5. Exit
    Enter your choice: '''))

    if c == 1:
        n = input("Enter the value:-- ")
        l.append(n)
        print("Stack:", l)

    elif c == 2:
        if len(l) == 0:
            print("Empty Stack")
        else:
            p = l.pop()
            print("Popped:", p)
            print("Stack after pop:", l)

    elif c == 3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print("Top of the Stack:", l[-1])

    elif c == 4:
        print("Current Stack:", l)

    elif c == 5:
        print("Exiting the Stack program. Bye!")
        break

    else:
        print("Invalid Operator entered....")
