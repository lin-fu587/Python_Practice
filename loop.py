#while迴圈
n=1
while n<5:  #假如條件式是布林值的True=>會變成無窮迴圈
    print(n)
    n=n+1

#1+2+3+4...+10(while版)
n=1
sum=0
while n<=10:
    sum=sum+n
    print("當前值為:",n)
    print("當前總和為:",sum)
    n=n+1

#for迴圈
for i in [3,5,1]:   #將列表中的值依序放入變數i，每一個皆跑一次
    print(i)
print("\n")

for x in "hello":   #將字串中的字元依序放入變數x，每一個字元皆跑一次
    print(x)
print("\n")

for j in range(5):  #從0開始依序放入，放到4，相當於c語言的for(j=0;j<5;j++)
    print(j)
print("\n")

for a in range(5,10):   #相當於c語言的for(a=5;a<10;a++)
    print(a)

#1+2+3+4...+10(for版)
sum2=0
for k in range(1,11):
    sum2=sum2+k
    print("當前值為:",k)
    print("當前總和為:",sum2)
