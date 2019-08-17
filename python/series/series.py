def slices(series, length):
    results = []
    if len(series) == 0 or length <= 0 or len(series) < length:
        raise ValueError("Please try again. The values do not fit \
        the purpose of the exercise")
    for i in range(0, len(series) - (length - 1)):
        my_slice = series[i:i+length]
        results.append(my_slice)
    return results
