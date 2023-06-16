def add(*args):
    sum1=0;
    for i in args:
        sum1+=i
    return sum1

print(add(1,2,3,4,5,6,7,8,9,10))


def calculate(**kwargs):
    for (key, value) in kwargs.items():
        print(key)
        print(value)

def calculate2(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(add=3, multiply=5)
calculate2(2,add=3, multiply=5)

