'''
1)
    Write a program which will find all such numbers which are divisible by 7
    but are not a multiple of 5, between 2000 and 3200 (both included).The
    numbers obtained should be printed in a comma-separated sequence on a
    single line.
'''


def exercise1():
    result = [num for num in range(2000, 3200)
              if num % 7 == 0 and num % 5 != 0]
    return result


print(exercise1())
print()

'''
2)
    Write a program which can compute the factorial of a given numbers.The
    results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program: 8 Then, the output
    should be:40320
'''


def exercise2(max):
    b = 1
    for num in range(max+1):
        if num == 0:
            num = 1
        b = num*b
        print(b, end="")
        if num < max:
            print(end=", ")
    print()


exercise2(8)
print()

'''
3)
    With a given integral number n, write a program to generate a dictionary
    that contains (i, i x i) such that is an integral number between 1 and n
    (both included). and then the program should print the dictionary.Suppose
    the following input is supplied to the program: 8

    Then, the output should be:

    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''


def exercise3(max):
    return {num: num*num for num in range(1, max+1)}


print(exercise3(8))
