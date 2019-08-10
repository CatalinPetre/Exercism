def is_armstrong(number):
    no_digits = len(str(number))
    armstrong_no = 0
    # i = number
    for i in str(number):
        armstrong_no = armstrong_no + int(i) ** no_digits
    print(armstrong_no)
    if number == armstrong_no:
        return True
    else:
        return False
