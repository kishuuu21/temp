q=0
def division(a,b):
    global q
    if b == 0:
        return " division by 0 not accepted "
    negative = (a<0) != (b<0)
    a,b = abs(a) , abs(b)
    while a >= b :
        a -= b
        q += 1
    return -q if negative else q
print(division(100,-20))