"""to find binary equivalent of a no throough recursion
"""
def binary(num):

    if num == 0:
        return

    binary(num//2)
    print(num % 2, end=" ")


number = 8
#print(bin(number))
binary(number)