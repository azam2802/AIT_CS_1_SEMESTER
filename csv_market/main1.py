# arr = [1,3,5,5,5,5,-23,-3]
# # def get_count_of_max(arr):
# #     mx = arr[0]
# #     for i in arr:
# #         if i > mx:
# #             mx = i
# #     return arr.count(mx)
# # print(get_count_of_max(arr))




# def count_negative_number(arr):
#     count = 0
#     for i in arr:
#         if i < 0:
#             count += 1
#     return count
# print(count_negative_number(arr))

# dict = {
#     "a": 10,
#     "b": 18,
#     "c": 234,
#     "d": 1
# }

# min = float("-inf")

names = [1,2,3,4,5]
amounts = [1000,20000,30000,4000,500]

def transfer(sender,reciever,amount):
    senderId = 0
    recieverId = 0
    for i,j in enumerate(names):
        if sender == j:
            senderId = i
        elif reciever == j:
            recieverId = i
    amounts[senderId] -= amount
    amounts[recieverId] += amount
    return amounts

print(transfer(1, 3, 100))