# from random import randint, shuffle


# def sum_prob():
#     count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     for _ in range(10000):
#         dice1 = randint(1, 6)
#         dice2 = randint(1, 6)
#         count[(dice1+dice2)-2] += 1
#     return [i/ 10000 for i in count]

# for i,v in enumerate(sum_prob()):
#     print(f"{"*"*int(v*100)} -> {i+2}, P: {round(v*100)}%")

# balls = [
#     "blue",
#     "blue",
#     "blue",
#     "green",
#     "green",
#     "green",
#     "green",
#     "green",
#     "blue",
#     "blue",
#     "blue",
#     "blue",
#     "blue",
#     "blue",
#     "blue",
# ]


# def balls_prob():
#     shuffle(balls)
#     count = 0
#     for _ in range(100):
#         ball1Index = randint(0, 14)
#         ball1 = balls[ball1Index]
#         ball2Index = randint(0, 14)
#         ball2 = balls[ball1Index]
#         if ball1 == "blue" and ball2 == "blue":
#             count += 1
#     balls.pop(ball1Index)
#     balls.pop(ball2Index)
#     return count / 100


# print(balls_prob())

# d = {"emil": 10}
# print(d.get())