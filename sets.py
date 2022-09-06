#sets don't allow for duplicate values

def belt_count(dictionary):
    belts = list(dictionary.values())
    
    #Cast as set to eliminate any duplicate values
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belt(s).')


ninja_belts = { }

while True:
    ninja_name = input("Enter the name: ")
    ninja_belt = input("Enter a belt color: ")
    ninja_belts[ninja_name] = ninja_belt

    another = input("Add another? (y/n)")

    if another == 'y':
        continue
    else:
        break

belt_count(ninja_belts)