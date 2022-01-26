# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 17:56:37 2022

@author: Setareh
"""
import re
import simple_calculator as smp
import advanced_calculator as adv
import scientific_calculator as sci
#calculator
#select your calculator
while True:
    print ("select your calculator")
    print ("a. simple")
    print ("b. advanced")
    print ("c. scientific")
    print ("e. exit")
    choice = input ("enter your choice (a/b/c/e): ")
    if choice == "a" :
        number1 = input("please return number 1 : ")
        number2 = input("please return number 2 : ")
        operator = input("please return op: ")
        num1 = int(number1)
        num2 = int(number2)
        i = smp.simple(num1, num2)
        if operator == "+":
           print(num1, '+', num2, '=', i.add())
        elif operator == "-":
            print(num1, '-', num2, '=', i.substract())
        elif operator == "*":
            print(num1, '*', num2, '=', i.multiply())
        elif operator == "/":
            print(num1, '/', num2, '=', i.divide())
        else :
            print ("invalid operator")
    elif choice == "b" :
        
        type=str( input("select your equation: "))
    
        for x in type:
            if x== "+" or x== "-" or x== "*" or x== "/" :
                operator = x.strip()
    
        num = re.findall(r'-?\d+\.?\d*', type)
        num1 = float(num[0])
        num2 = float(num[1])
    
        j = adv.advanced(num1, num2)
        if operator == "+":
           print(num1, '+', num2, '=', j.add())
        elif operator == "-":
            print(num1, '-', num2, '=', j.substract())
        elif operator == "*":
            print(num1, '*', num2, '=', j.multiply())
        elif operator == "/":
            print(num1, '/', num2, '=', j.divide())
        else :
            print ("invalid operator")
    
    elif choice == "c" :
        print("choose operation")
        print("1. arithmetic operation")
        print("2. advanced operation") 
        choice = input ("enter your choice (1/2) ")
        if choice == "1" :
            
            number1 = input("please return number 1 : ")
            number2 = input("please return number 2 : ")
            operator = input("please return op: ")
            num1 = int(number1)
            num2 = int(number2)
            k= sci.scientific(num1, num2)    
            if operator == "+":
               print(num1, '+', num2, '=', k.addition())
            elif operator == "-":
                print(num1, '-', num2, '=', k.subtract())
            elif operator == "*":
                print(num1, '*', num2, '=', k.multiply())
            elif operator == "/":
                print(num1, '/', num2, '=', k.divide())
            elif operator == "**":
                print(num1, '**', num2, '=', k.exponent())
            else :
                print ("invalid operator")
                
        if choice == "2" :
            number1 = input("please return number 1 : ")
           
            operator = input("please return op: ")
            num1 = int(number1)
           
            q=sci.second_scientific(num1)
            if operator == "log":
                 print('log', num1, '=', q.log())
            elif operator == "cos":
                 print('cos', num1, '=', q.cos())
            elif operator == "sin":
                 print('sin', num1, '=', q.sin()) 
            elif operator == "tan":
                 print('tan', num1, '=', q.Stan())
            else :
                print ("invalid operator")
    elif choice == "e":
        break                
    else :
        print ("invalid input")