arr = [] 
def fib(n): 
    arr.append(1) 
    arr.append(1) 
    for i in range(2,2*n+1): 
        arr.append((arr[i-1] + arr[i-2])%(10**9+7)) 
n = int(input()) 
sum = 0 
fib(n) 
if n%2==1: 
    sum = sum + arr[n-1]*arr[n-1] 
    n-=1 
for i in range(1,n,2): 
    sum =(sum+arr[2*i])) 
print(sum)
