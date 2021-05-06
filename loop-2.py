#1.break    #強制結束迴圈
n=1
while n<5:
    if n==3:
        break
    print(n)    #印出1和2
    n=n+1
print(n)    #印出3
print("\n")

#2.continue     #跳過continue下方指令，強制進行判斷下一次迴圈
a=0
for x in range(0,4):
    if x%2==1:
        continue
    print(x)
    a=a+1
print("跑內部的次數:",a)
#3.#else=>搭配迴圈時代表迴圈跑完全部後，還要再執行一次else中的內容
sum=0
for i in range(1,11):
    sum=sum+i
    print(i,sum)
else:
    print(sum)
#4.找出整數平方根
j=0
k=0
while k==0: 
    b=int(input("請輸入一個數值:"))
    for j in range(b+1):
        if  j*j==b&b!=0:
            print(b**0.5)
            break   #用break強制結束，不會跑else
        else:
            continue
    else:    
        print("沒有整數的平方根")
    z=int(input("請問是否還要繼續輸入，否請按1，其餘皆為繼續輸入\n=>"))
    if z==1:
        break
