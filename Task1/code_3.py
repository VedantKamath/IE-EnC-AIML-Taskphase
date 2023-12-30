i_1 = int(input("Ask your question and press = to get the answer :"))
while True :
        sign = input("")
        if (sign == "+"):
            i_2 = int(input(""))
            i_1+=i_2
        elif (sign == "-"):
            i_2 = int(input(""))
            i_1-=i_2
        elif (sign == "*"):
            i_2 = int(input(""))
            i_1*=i_2
        elif (sign == "/"):
            i_2 = int(input(""))
            i_1/=i_2
        elif (sign == "="):
            print(i_1)
            break
        else:
            print("your given sgn is not valid.")
