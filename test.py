print("Hello, world!\n")  # test1

print(2.4543543545454)  # test 2
print("%.1f" % 2.4543543545454)
print("%.2f" % 2.4543543545454)
print("%.3f" % 2.4543543545454)
print("%.4f" % 2.4543543545454)

print('H')  # test3
print('e')
print('l')
print('l')
print('o')
print('H'+'e'+'l'+'l'+'o')
print('Hello,world!')

print("Decimal: %d" % 255)  # test4
print("Hexadecimal: %x" % 255)
print("Hexadecimal: %X" % 255)
print("Octal: %o" % 255)

IDEALIC_METRIC_METER = int(1)  # test5
PI = float(3.14)
c = 'A'

print(IDEALIC_METRIC_METER)
print(PI)
print(c)

IDEALIC_METRIC_METER = int(2)
PI = float(3.15)
c = 'B'

print("\n")
print(IDEALIC_METRIC_METER)
print(PI)
print(c)

IDEAL_METRIC_METER = int(input())  # test6
car_length = float(input())
_char = input()

print(IDEAL_METRIC_METER)
print(car_length)
print(_char)

a = float(input())  # test7
x = float(input())
g = a+x
print("g=",g)
g = a+x*a
print("g1=",g)
g = (a+x)*a
print("g2=",g)
g = (a+x)/3.5
print("g3=",g)
g = (a+x)/(2+a)
print("g4=",g)
g = g/10
print("g5=",g)

import math  # test8

a = float(input())
x = float(input())
g = math.sin(a*x)*math.cos(a-x)
print("g=",g)

import math  # test9

x = int(input())
g = math.log(x)/math.log(2)
print('g=',g)

import math  # test10

a = float(input())
x = float(input())

G = -1*((2*(-5*a*a+3*a*x+2*x*x)/(5*a*a+9*a*x-2*x*x)))
F = math.sin(math.pi*(10*a*a+37*a*x+7*x*x))/math.pi*(10*a*a+37*a*x+7*x*x)
Y = math.log(-5*a*a-16*a*x+16*x*x+1)/math.log(2.0)

print("G=%.8f" % G)
print("F=%.8f" % F)
print("y=%.8f" % Y)
