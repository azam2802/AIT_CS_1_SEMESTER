arr = [1,2,3,4,5,6,7,8,9,0]
# def isEven(arr):
#     for i in arr[::-1]:
#         if i % 2 == 0:
#             arr.remove(i)
#             arr.insert(1,i)
#     for i in arr:
#         if i % 2 != 0:
#             arr.remove(i)
#             arr.append(i)
#     return arr

# # print(isEven(arr))


# def isEven(x):
#   if x % 2 != 0:
#     return False
#   else:
#     return True
  
# def isOdd(x):
#   if x % 2 == 0:
#     return False
#   else:
#     return True
  
# arr += filter(isEven, arr)
# arr += filter(isOdd, arr)
# arr = arr[10:]
# print(arr)

romanNums = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

number = 'DCCC'
res = 0
number = list(number)

for i, v in enumerate(number):
    if i < len(number)-1:
        if romanNums[v] * 5 == romanNums[number[i+1]] or romanNums[v] * 10 == romanNums[number[i+1]]:
            res += romanNums[number[i+1]] - romanNums[v]
            number.pop(i+1)
            number.remove(v)
            print(number, 1)
        else:
            res += romanNums[v]
            print(number,2)
    else:
        res += romanNums[v]
        print(number,3)
print(res)