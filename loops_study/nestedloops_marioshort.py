def main():
    print_square(5)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()



#def main():
    #print_square(3)


#def print_square(size):
    #for i in range(size):
        #print("#" * size)


#main()