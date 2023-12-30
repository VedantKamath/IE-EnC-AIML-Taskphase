def count_char(str1) :
    str1 = str1.replace(" ","")
    count = 0
    i = 0
    for i in str1:
        count+=1
    return count

string = count_char('My name is Vedant')
print(string)