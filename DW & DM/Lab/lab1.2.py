num = int(input())
reverse = 0
while(num>0):
    a=num%10
    reverse=reverse*10+a
    num = num//10
print(reverse)
