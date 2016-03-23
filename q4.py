a = input("請輸入：")
i = 0
while True:
    if a[i]==a[len(a)-i-1]:
        i = i+1

    else:
        print("不是回文")
        break
    if i==len(a)-1:
        print("回文")
        break

'''
#索引值   abc cba
         123 456

i=0
abccba[0]?= abccba[5]
long=len(abccba)
i=0: long-i-1=6-0-1=5
i=1: long-i-1=6-1-1=4
'''
'''
s = input("請輸入字串：")
current = len(s) - 1
flag = False
while current != 0:
    if s[current] == s[len(s) - current - 1]:
        flag = True
    else:
        flag = False
        break
    current -=1
print(flag)
