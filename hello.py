'''
x=3
if x<0:
    print('x<0')
elif x==0:
    print('x==0')
else:
    print('x>0')
'''

'''
s = [1,3,5,7,9]
for i in s:
    print(i)
'''
'''
s = [2,4,6,8,10]
for i in range(len(s)):
    print('i=',i,s[i]);
'''
'''
print(list(range(10)))
'''
'''
def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()

fib(100000)

print(fib(1000))
'''
'''
i = 5
def f(arg=i):
    print(arg)

i = 6
f()
'''
'''
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
'''


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(122,'22')
