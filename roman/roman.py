
ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
nums = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

def roman(number):
    s = ""  # result string
    for i in range(len(ints)):
        c = number // ints[i]
        s += nums[i] * c
        number -= (ints[i] * c)
    return s
