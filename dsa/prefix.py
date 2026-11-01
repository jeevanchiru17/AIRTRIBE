arr = [8, 2, 3, 4, 5, 6, 4]
prefixSum = [0 for i in range(len(arr))]

prefixSum[0] = arr[0]

for i in range(1, len(prefixSum)):
  prefixSum[i] = prefixSum[i - 1] + arr[i]
print(prefixSum)

## and hash ing
for i in arr:
    