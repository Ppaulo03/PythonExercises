'''
4)
    Write a program which accepts a sequence of comma-separated numbers from
    console and generate a list and a tuple which contains every number.Suppose
    the following input is supplied to the program:

    34, 67, 55, 33, 12, 98
    Then, the output should be:

    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
'''


def exercise4():
    seq = str(input('Write a sequence of comma-separated numbers: '))
    num = ''
    lista = []
    for char in seq:
        if char == ',':
            try:
                lista.append(str(int(num)))
            except ValueError:
                pass
            finally:
                num = ''
        else:
            num += char
    try:
        lista.append(str(int(num)))
        num = ''
    except ValueError:
        pass

    tup = tuple(lista)
    return lista


'''
5)
    Define a class which has at least two methods:

        * getString: to get a string from console input
        * printString: to print the string in upper case.

    Also please include simple test function to test the class methods.
'''


def exercise5():
    class UseString():
        def __init__(self):
            self.text = ''

        def getString(self):
            self.text = input("Write something: ")

        def printString(self, text=''):
            if text == '':
                text = self.text
            print(text.upper())

    test = UseString()
    test.getString()
    test.printString()
    test.printString('anything')


'''
6)
    Write a program that calculates and prints the value according to the
    given formula:

    Q = Square root of [(2 * C * D)/H]

    Following are the fixed values of C and H:

    C is 50. H is 30.

    D is the variable whose values should be input to your program in a
    comma-separated sequence.For example Let us assume the following comma
    separated input sequence is given to the program:

    100,150,180
    The output of the program should be:

    18,22,24
'''


def exercise6():
    C, H = 50, 30
    D = [int(n) for n in exercise4()]
    Q = [int(((2 * C * n) / H) ** 0.5) for n in D]
    print(Q)


'''
7)
    Write a program which takes 2 digits, X,Y as input and generates a
    2-dimensional array. The element value in the i-th row and j-th column of
    the array should be i * j.

    Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to
    the program: 3,5


    Then, the output of the program should be:

    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''


def exercise7():
    def get_int(text):
        while True:
            try:
                print()
                num = int(input(f"{text}: "))
            except ValueError:
                print('Just ints, please')
            else:
                return num

    x = get_int('X')
    y = get_int('Y')

    output = []
    for row in range(x):
        lista = [collumn*row for collumn in range(y)]
        output.append(lista)
        lista.clear
    print(output)


'''
8)
    Write a program that accepts a comma separated sequence of words as input
    and prints the words in a comma-separated sequence after sorting them
    alphabetically.

    Suppose the following input is supplied to the program:

    without,hello,bag,world
    Then, the output should be:

    bag,hello,without,world

'''


def exercise8():
    sequence = input('write a comma separated sequence of words: ').split(',')
    seequence = sequence.sort()
    print(sequence)


'''
9)
    Write a program that accepts sequence of lines as input and prints the
    lines after making all characters in the sentence capitalized.

    Suppose the following input is supplied to the program:

    Hello world
    Practice makes perfect

    Then, the output should be:

    HELLO WORLD
    PRACTICE MAKES PERFECT
'''


def exercise9():
    text = []
    while True:
        sentence = input()
        if sentence == '':
            break
        text.append(sentence.upper())

    for line in text:
        print(line)
