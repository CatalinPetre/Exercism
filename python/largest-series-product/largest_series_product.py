def slices(series, length):
    results = []
    if length == 0:
        return 1
    elif len(series) == 0 or length < 0 or len(series) < length:
        raise ValueError("The series needs to have more than one element, \
        the size needs to be a positive number and shorter than \
        the length of the series. Please try again.")
    for i in range(0, len(series) - (length - 1)):
        my_slice = series[i:i+length]
        results.append(my_slice)
    return results


def largest_product(series, length):
    results = slices(series, length)
    if results == 1:
        return 1
    prod_list = []
    for my_slice in results:
        int_my_slice = [int(j) for j in my_slice]
        prod = 1
        for i in int_my_slice:
            prod = prod * i
        prod_list.append(prod)
    return max(prod_list)
