# converts array of ints to int, adds n, 
# and creates new array
def add_array(a, n):
    if len(a) == 0:
        return None

    result = n + array_to_int(a)
    return int_to_array(result, len(a))

def array_to_int(a):
    exponent = len(a) - 1
    result = 0
    for num in a:
        result += num  * (10 ** exponent)
        exponent -= 1

    return result

def int_to_array(n, array_size):
    # need new array length if sum has more digits than a
    n_digits = get_digits(n)
    if n_digits > array_size:
        array_size = n_digits

    result = [0] * array_size

    temp = n
    # start pos for inserting new nums
    i = len(result) - 1  
    while temp > 0:
        # get rightmost digit
        digit = temp % 10
        result[i] = digit

        # remove rightmost digit
        temp = temp // 10
        i -= 1

    return result

def get_digits(n):
    temp = n
    digits = 0
    while temp > 0:
        temp = temp // 10
        digits += 1

    return digits
