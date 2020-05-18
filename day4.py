'''
14)
    Write a program that accepts a sentence and calculate the number of upper
    case letters and lower case letters.

    Suppose the following input is supplied to the program:

    Hello world!
    Then, the output should be:

    UPPER CASE 1
    LOWER CASE 9
'''


def exercise14():
    sentence = input('Write a sentence: ')
    upper, lower = 0, 0
    for char in sentence:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1

    print(f'UPPER CASE {upper}')
    print(f'LOWER CASE {lower}')


'''
15)
    Question:
    Write a program that computes the value of a+aa+aaa+aaaa with a given
    digit as the value of a.

    Suppose the following input is supplied to the program:

    9
    Then, the output should be:

    11106
'''


def exercise15(n):
    while True:
        try:
            num = int(input("Write a single algarism: "))
            if -10 < num < 10:
                break
            else:
                print("That's not an single algarism...")
        except ValueError:
            print("That's not an algarism...")

    num = str(num)
    soma = 0
    for i in range(1, n):
        soma += int(num*i)
    print(soma)
