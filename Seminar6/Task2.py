# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
from sympy import fibonacci
print([fibonacci(i) for i in range(1,int(input())+1)])
