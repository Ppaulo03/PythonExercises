'''
10)
    Write a program that accepts a sequence of whitespace separated words as
    input and prints the words after removing all duplicate words and sorting
    them alphanumerically.

    Suppose the following input is supplied to the program:

    hello world and practice makes perfect and hello world again

    Then, the output should be:

    again and hello makes perfect practice world
'''


def exercise10():
    word = input().split()

    for i in word:
        if word.count(i) > 1:
            word.remove(i)

    word.sort()
    print(" ".join(word))


'''
11)
    Write a program which accepts a sequence of comma separated 4 digit binary
    numbers as its input and then check whether they are divisible by 5 or not.
    The numbers that are divisible by 5 are to be printed in a comma separated
    sequence.

    Example:

    0100,0011,1010,1001
    Then the output should be:

    1010
    Notes: Assume the data is input by console.
'''


def exercise11():
    data = input().split(',')
    data = list(filter(lambda i: int(i, 2) % 5 == 0, data))
    print(",".join(data))


'''
12)
    Write a program, which will find all such numbers between 1000 and 3000
    (both included) such that each digit of the number is an even number.The
    numbers obtained should be printed in a comma-separated sequence on a
    single line.
'''


def exercise12(n_min=1000, n_max=3000):
    nums = []
    for n in range(n_min, n_max+1):
        all_even = True
        separated = [digito for digito in str(n)]
        for digito in separated:
            if int(digito) % 2 != 0:
                all_even = False
                break
        if all_even:
            nums.append(str(n))
    print(','.join(nums))


'''
13)
    Write a program that accepts a sentence and calculate the number of
    letters and digits.

    Suppose the following input is supplied to the program:

    hello world! 123
    Then, the output should be:

    LETTERS 10
    DIGITS 3
'''


def exercise13():
    letter, digit = 0, 0
    sentence = input('Sentence: ')
    for char in sentence:
        letter += char.isalpha()
        digit += char.isnumeric()
    print(f"LETTERS {letter}\nDIGITS {digit}")
