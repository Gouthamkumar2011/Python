# #Problem 1

# def arraycheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i] ==1 and  nums[i+1] ==2 and  nums[i+2] ==3:
#             return True
#     return False

# print(arraycheck([1,1,2,4,1]))

# #Problem 2
# def stringBits(mystring):
#     result = ""

#     for i in range(len(mystring)):
#         if i%2 == 0:
#             result = result + mystring[i]
#     return result

# print(stringBits("Heeololeo"))

# #Problem 3

# def end_other(a,b):
#     a = a.lower()
#     b = b.lower()
#     return a[-(len(b)):] == b or a == b[-(len(a)):]

# print(end_other('Hiabc','abc'))

# #Problem 4

# def Doublechar(mystring):
#     result = ''
#     for char in mystring:
#         result += char*2

#     return result

# print(Doublechar("Hi, Hello"))


# def no_teen_sum(a,b,c):
#     return fixteen(a) + fixteen(b) + fixteen(c)

# def fixteen(n):
#     if n == (13,14,17,18,19):
#         return 0
#     return n

# print(no_teen_sum(17,2,3))

def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if i%2 == 0:
            count+=1
    return count

print(count_evens([2,2,0]))