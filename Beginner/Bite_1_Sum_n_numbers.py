def sum_numbers(numbers=None):
    total = 0

    if numbers == None:
        for i in range(1,101):
            total += i
        print (total)
        return total
    else:
        return sum(numbers)
    
    #other solution
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)


def test_sum_numbers_default_args():
    assert sum_numbers() == 5050
    assert sum_numbers(numbers=None) == 5050


def test_sum_numbers_various_inputs():
    assert sum_numbers(range(1, 11)) == 55
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers((1, 2, 3)) == 6
    assert sum_numbers([]) == 0  # !! [] not the same as None


print (test_sum_numbers_default_args ())
