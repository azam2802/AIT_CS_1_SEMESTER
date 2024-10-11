from random import randint
money = 100
count = 0 
while money < 1000:
    roll = randint(0,10)
    money = money + 2 if roll <= 3  else money - 1
    count += 1
    print(money, roll < 3)
print(count)
    