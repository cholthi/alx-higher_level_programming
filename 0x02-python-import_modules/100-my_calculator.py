#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    if len(argv) < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    operand1 = argv[1]
    op = argv[2]
    operand2 = argv[3]

    if op not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    if op == '+':
        print('{} {} {} = {}'.format(operand1, op, operand2, add(
            int(operand1), int(operand2))))
    elif op == '-':
        print('{} {} {} = {}'.format(operand1, op, operand2, sub(
            int(operand1), int(operand2))))
    elif op == '*':
        print('{} {} {} = {}'.format(operand1, op, operand2, mul(
            int(operand1), int(operand2))))
    elif op == '/':
        print('{} {} {} = {}'.format(operand1, op, operand2, div(
            int(operand1), int(operand2))))
