import math  # test10

a = float(input())
x = float(input())

G = -1*((2*(-5*a*a+3*a*x+2*x*x)/(5*a*a+9*a*x-2*x*x)))
F = math.sin(math.pi*(10*a*a+37*a*x+7*x*x))/math.pi*(10*a*a+37*a*x+7*x*x)
Y = math.log(-5*a*a-16*a*x+16*x*x+1)/math.log(2.0)

print("G=%.8f" % G)
print("F=%.8f" % F)
print("y=%.8f" % Y)