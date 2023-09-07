mylist = []

for i in range (0,10):
    mylist.append(i)

# def evenbool(num):
#     return num%2 == 0

evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))

