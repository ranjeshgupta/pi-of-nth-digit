def pi(n):
    '''
    :argument n integer to generate pi up to nth decimal point
    :return: float | string
    '''
    try:
        n = int(n)
    except:
        return "Please intput integer to generate pi up to this digit"
    else:
        return round((22.00 / 7.00), n)

while True:
    print("Find PI to the Nth decimal")
    try:
        digit = int(input("Please enter number of digit: "))
    except:
        print ("Invalid digit to find PI to the Nth decimal")
        continue
    else:
        value_of_pi = pi(digit)
        print("PI to {d}th decimal is {x:1.{d}f}".format(x=value_of_pi, d=digit))
        break
