arr1 = [1, 4, 5, 10]
arr2 = [2, 7, 8, 30]
arr3 = arr1 + arr2
arr4 = []
for i, v in enumerate(arr3):
    if i < len(arr3):
        arr4.append(min(arr3[i+1::]))

print(arr4)
