def calc(*args):
    pass
    #print(args)
    if len(args) == 3:
        pass
    if args[0] == 'r':
        pass
        area = float(args[1] * args[2])
        #print("\nYour shape is Rectangle.\nIt`s area is {0}".format(area, 0))
    if args[0] == 't':
        pass
        area = float(0.5 * args[1] * args[2])
        #print("\nYour shape is Triangle.\nIt`s area is {0}".format(area, 0))
    if len(args) == 2:
        pass
    if args[0] == 's':
        pass
        area = float(args[1] * args[1])
        #print("\nYour shape is Square.\nIt`s area is {0}".format(area, 0))
    if args[0] == 'c':
        pass
        area = float(3.14 * args[1] * args[1])
        #print("\nYour shape is Circle.\nIt`s area is {0}".format(area, 0))
    return area

# shape = input("Enter the shape: ")
# calcArea(shape, 2, 5)