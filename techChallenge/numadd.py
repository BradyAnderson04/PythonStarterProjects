# 31 is 6 

arr = [2, 5, 7, 12, 19, 31]

# sum = arr[n-1] + arr[n-2]

for i in range(6, 41):
    arr.append(arr[i-1] + arr[i-2])
    sum = arr[i-1] + arr[i-2]
    print(sum)
    if(i == 40):
        print(arr[i-1] + arr[i-2])