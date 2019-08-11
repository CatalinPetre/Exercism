def largest_product(series, size):
    largest_prod = 0
    for i in series:
        prod = series(i) * series(i+1) * series(i+2)
        if prod > largest_prod:
            largest_prod = prod
        i = i + 1
