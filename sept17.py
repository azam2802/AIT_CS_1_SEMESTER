arr = [0, 12, 3, 4, 5, 6, 7, 8]
arr_odd = [0, 11, 3, 5, 7]

# def aliya(x):
#     y = x*x
#     z = x//2
#     return y, z
# print(aliya(10))


# def check():
#     for i in arr_odd:
#         if i % 2 == 0:
#             return True
#     return False
# print(check())

# def find_pairs_with_sum(arr, target):
#     result = []
#     n = len(arr)

#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target:
#                 if arr[i] < arr[j]:
#                     result.append((arr[i], arr[j]))

#     return result

# arr = [1, 3, 2, 4, 5, 6]
# target = 7
# print(find_pairs_with_sum(arr, target))

# def uncommonFromSentences(s1, s2):
#     spl1, spl2 = s1.split(), s2.split()
#     res = []
#     for i, v in enumerate(spl1):
#         if spl1[i] != spl2[i]:
#             res.append(spl1[i])
#             res.append(spl2[i])
#     print(res)
# uncommonFromSentences("this apple is sweet", "this apple is sour")