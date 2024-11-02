arr = [["Emil", 20,30], ["azam", 2]]

arr = sorted(arr, key=lambda x: sum(x[1:]), reverse = True)

print(arr)