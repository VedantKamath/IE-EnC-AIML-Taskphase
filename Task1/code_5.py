a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
if (a > b) and (a > c) :
    print(a ,("is the largest"))
elif (b > c) and (b > a) :
    print(b ,("is the largest"))
elif (c > b) and (c > a) :
    print(c ,("is the largest"))
if (b < c) and (b < a) :
    print(b ,("is the smallest"))
elif (c < b) and (c < a) :
    print(c ,("is the smallest"))
elif (a < c) and (a < b) :
    print(a ,("is the smallest"))