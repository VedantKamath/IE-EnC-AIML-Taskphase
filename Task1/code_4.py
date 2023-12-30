n = int(input("Enter number of integers :"))
l = []
i = 0
sum = 0
print("Enter your integer list")
for i in range(n) :
    t = int(input())
    l.append(t)
    sum+=t

avg = sum/n
print(l)
print("The average is ")
print(avg)