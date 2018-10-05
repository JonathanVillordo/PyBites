def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    return [i for i in numbers if i > 0 and i%2 == 0 ]


print(filter_positive_even_numbers(list(range(-10, 11))))
