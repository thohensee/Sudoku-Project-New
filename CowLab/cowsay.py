import sys
from heifer_generator import HeiferGenerator
from dragon import Dragon

def list_cows(cows):
    print("Available cows: ", end = "")
    for cow in cows:
        print(cow.name, end = " ")

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

if __name__ == '__main__':
    cows = HeiferGenerator.get_cows()

    if sys.argv[1] == '-l':
        list_cows(cows)

    elif sys.argv[1] == '-n':
        cow = find_cow(sys.argv[2], cows)
        if cow == None:
            print(f"Could not find {sys.argv[2]} cow!")
        else:
            for i in range(3, len(sys.argv)):
                print(sys.argv[i], end = " ")
            print()
            cow.set_image(cow.image)
            print(cow.get_image())
            if isinstance(cow, Dragon):
                if cow.can_breathe_fire():
                    print("This dragon can breathe fire.")
                else:
                    print("This dragon cannot breathe fire.")
    else:
        cow = find_cow('heifer', cows)
        for i in range(1, len(sys.argv)):
            print(sys.argv[i], end=" ")
        print()
        cow.set_image(cow.image)
        print(cow.get_image())