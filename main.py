
import math
a=int(input())
b=int(input())
c=int(input())
d=(b**2-4*a*c)
print(d)
if d<0:
    print('Нет корней')
if d==0:
    x=((-b)/(2*a))
if d>0:
    print('x=', x)
    x1=((-b)-((d)**(0.5)))/(2*a)
    x2=((-b)+((d)**(0.5)))/(2*a)
    print('x1=', x1, 'x2=', x2)
