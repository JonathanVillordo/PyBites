VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        color = input('Enter a Color: ')
        if color.lower() =='quit':
            print ('bye')
            break
        if color.lower()  in VALID_COLORS:
            print(color.lower())
        else:
            print('Not Valid')
            continue

print_colors()
