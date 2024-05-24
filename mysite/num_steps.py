N = int(input())
data = [int(x) for x in input().split()]
# data = [int(x) for x in range(N): input.split()]
print(data)
num=0
for x in data:
    num = num*10 +x%10

if num%10 == 0:
    print("Yes")
else:
    print("No")