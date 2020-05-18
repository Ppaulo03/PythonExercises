'''
16)
    Use a list comprehension to square each odd number in a list. The list is
    input by a sequence of comma-separated numbers. >Suppose the following
    input is supplied to the program:

    1,2,3,4,5,6,7,8,9

    Then, the output should be:

    1,9,25,49,81

'''


import pdb


def exercise15():
    while True:
        lista = input(
            "Write a sequence of comma-separated numbers: ").split(",")
        try:
            for n in lista:
                num = int(n)
            break
        except ValueError:
            print("Only interger numbers, please")
            print()

    squared_odd = [int(n)**2 for n in lista if int(n) % 2]
    print(squared_odd)


'''
16)
    Write a program that computes the net amount of a bank account based a
    transaction log from console input. The transaction log format is shown as
    following:

    D 100
    W 200

    D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program:

    D 300
    D 300
    W 200
    D 100

    Then, the output should be:

    500
'''


def exercise16():
    bank = 0
    while True:
        value = input().split(" ")
        try:
            if value == ['']:
                break
            elif len(value) > 2:
                print("Use apenas 2 componentes no comando")
            elif value[0] == 'D':
                bank += float(value[1])
            elif value[0] == 'W':
                bank -= float(value[1])
            else:
                print("Utilise apenas as operações padrões: 'D' e 'W'")
        except ValueError:
            print("Por favor use apenas números após a operação")
    print(bank)
