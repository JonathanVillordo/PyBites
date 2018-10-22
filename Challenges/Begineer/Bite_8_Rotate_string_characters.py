import collections

''' Write a function that rotates characters in a string, in
    bot directions
'''

def rotate (string, n):
    """ Rotate characters in a string. Expects string and n (int) for
    number of characters to move
     solution 2 return string[n:] + string[:n]
    """
    word = collections.deque(string)
    neword = ''

    for letter in string[:n]:
        word.popleft()
        word.append(letter)

    return ''.join(word)
