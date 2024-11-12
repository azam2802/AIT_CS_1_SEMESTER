from time import time
from random import randint

a = [[randint(10,100) for i in range(1000)] for i in range(1000)]

resA = []
stride = 10
st = time()

for i in a:
    total_sum = 0
    for j in range(stride):
        total_sum += sum(i[j::stride])
    resA.append(total_sum)

end = time()
tA = end - st

print(resA)
print("\ntime:",tA)
print("check:", sum(a[-1]))

# resA = []
# stride = 10
# st = time()
# for i in a:
#     total_sum = 0
#     for j in i:
#         total_sum += j
#     resA.append(total_sum)
# end = time()
# tA = end - st
# print(resA)
# print("time:",tA)
# print("check:", sum(a[-1]))


# resB = []
# st = time()
# for i, n in enumerate(a):
#     sum = 0
#     for j in n:
#         sum += a[j][i]
#     resB.append(sum)
# end = time()

# tB = end-st
# print(time())
# print("resA", tA)
# print("resB", tB)