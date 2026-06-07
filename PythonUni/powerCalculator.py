def exponent(base, exp):
    tavan = exp
    result = 1
    while tavan > 0:
        result = result * base
        tavan = tavan - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(2, 3)