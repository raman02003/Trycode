arr = [12, 11, 13, 5, 6]
for i in range(1, len(arr)):
    for j in range(0, len(arr)-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)