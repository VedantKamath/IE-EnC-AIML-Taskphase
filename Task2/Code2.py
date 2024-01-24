num = 100

def fact_fn(n) :
    if (n==1) :
        return n
    else :
        return n* fact_fn(n-1)

print(fact_fn(num))
