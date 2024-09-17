numbers=[1,7,33,6,88,-7,25,13,7]
even=[]
odd=[]
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


print(even)