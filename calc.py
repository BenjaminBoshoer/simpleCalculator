import re
from time import time
#import tkinter as tk

def solve_add(str1):
    sum = 0

    # This is the recursive calling for solve_add(), calls solve_add() while there are + signs
    sum_list = str1.split('+')
    if len(sum_list) != 1:
        for i in sum_list:
            sum += solve_add(i)

    # This Else statement handles the parts in between the sums
    else:
        p = 1
        product_list = str1.split('*')
        if len(product_list) == 1:
            if '/' in product_list[0]:
                sum = divide_list(product_list[0])

            else:
                sum = float(str1)

        else:
            for j in product_list:
                if '/' in j:
                    p *= divide_list(j)

                else:
                    div=1
                    p *= float(j)

            sum = float(p)

    return sum

def divide_list(str1):
    div_list = str1.split('/')
    div = float(div_list[0])
    for k in range(len(div_list) -1):
        if div_list[k+1] == '0':
            exit("Division by zero")
        div /= float(div_list[k+1])

    return div

def handle_brackets(str1):

    open = list()
    close = 0
    flag = 1

    if str1.count('(') != str1.count(')'):
        return("Bracket Error")

    if '(' in str1:
        while flag == 1:
            flag = 0
            i=0
            open = list()
            for i in range(len(str1)):
                if str1[i] == '(':
                    open.append(int(i))

                if str1[i] == ')':
                    to_replace = str1[open[-1]+1:i]
                    str1 = str1.replace('('+to_replace+')', str(solve_add(to_replace)))
                    flag = 1
                    break



    return solve_add(str1)

def solve(str1):
    flag = 0
    if str1 == '':
        return 'Empty Input'

    str1 = str1.replace(" ","")


    for i in range(len(str1)-1):
        if str1[i].isalpha() == True:
            flag = 1

        elif str1[i] == '+' or str1[i] == '-' or str1[i] == '*' or str1[i] == '/':
            if str1[i+1] == '+' or str1[i+1] == '-' or str1[i+1] == '*' or str1[i+1] == '/':
                flag = 1


    if len(str1) == 1:
        if str1.isalpha() == True:
            flag = 1

    if flag == 1:
        return "Input Error"

    if(str1[0] == '-'):
        str1 = '0'+str1
    str1 = str1.replace("-","+-")
    str1 = str1.replace("*+-", '*-')
    str1 = str1.replace("/+-", '/-')


    str1 = handle_brackets(str1)

    return str1

def main():
    print("Simple calculator. enter -1 to exit")
    str1 = 0
    while str1 != '-1':
        print(">>> ", end= "")
        str1 = input()
        t0 = time()
        print(f'{solve(str1)}')
        t1 = time()
        print(f"{float(t1-t0)}")

if __name__ == "__main__":
    #window = tk.Tk()
    main()
