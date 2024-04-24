from Pakudex import pakudex
from Pakudex import pakuri

# HW 5-6 - Pakudex

def main():

    print('Welcome to Pakudex: Tracker Extraordinaire!')

    while True:
        try:
            capacity = int(input('Enter max capacity of the Pakudex: '))
            print(f'The Pakudex can hold {capacity} species of Pakuri.\n')
            break
        except ValueError:
            print('Please enter a valid size.')

    _pakudex = pakudex.pakudex(capacity)

    while True:
        print('Pakudex Main Menu\n'
            '-----------------\n'
            '1. List Pakuri\n'
            '2. Show Pakuri\n'
            '3. Add Pakuri\n'
            '4. Evolve Pakuri\n'
            '5. Sort Pakuri\n'
            '6. Exit\n')

        choice = input('What would you like to do? ')

        match choice:
            case '1':
                if _pakudex.get_size() == 0:
                    print('No Pakuri in Pakudex yet!\n')
                else:
                    print('Pakuri In Pakudex:')
                    species_array = _pakudex.get_species_array()
                    num = 1

                    for item in species_array:
                        print(str(num) + '. ' + item + '')
                        num += 1

                    print()
            case '2':
                species = input('Enter the name of the species to display: ')
                species_array = _pakudex.get_species_array()

                if species in species_array:
                    stats = _pakudex.get_stats(species)

                    print(f'\nSpecies: {species}')
                    print(f'Attack: {stats[0]}')
                    print(f'Defense: {stats[1]}')
                    print(f'Speed: {stats[2]}\n')
                else:
                    print('Error: No such Pakuri!\n')
            case '3':
                if _pakudex.get_size() == capacity:
                    print('Error: Pakudex is full!\n')
                else:
                    species = input('Enter the name of the species to add: ')
                    species_array = _pakudex.get_species_array()

                    if species not in species_array:
                        _pakudex.add_pakuri(species)
                        print(f'Pakuri species {species} successfully added!\n')
                    else:
                        print('Error: Pakudex already contains this species!\n')
            case '4':
                species = input('Enter the name of the species to evolve: ')
                species_array = _pakudex.get_species_array()

                if species in species_array:
                    _pakudex.evolve_species(species)
                    print(f'{species} has evolved!\n')
                else:
                    print('Error: No such Pakuri!\n')
            case '5':
                _pakudex.sort_pakuri()
                print('Pakuri have been sorted!\n')
            case '6':
                print('Thanks for using Pakudex! Bye!')
                exit()

        try:
            choice = int(choice)

            if choice not in range(1,7):
                print('Unrecognized menu selection!\n')
        except:
            print('Unrecognized menu selection!\n')

if __name__ == '__main__':
    main()