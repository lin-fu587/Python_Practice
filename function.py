#function define
#函式沒有呼叫，內部程式碼不會執行
def multiply():
    print(3*4)

def multiply2(n1,n2):   #在python中的冒號相當於c語言的大括弧
    print(n1*n2)
    return  #後面沒給回傳值的return或是沒寫return都回傳none

def multiply3(x1,x2):
    print(x1*x2)
    return x1*x2

#function call
multiply()
multiply2(10,8)

#回傳值 return
value=multiply2(2,3)
print(value)

print(multiply3(3,4))

#回傳值優點=>適用於繼續在主程式中操作回傳的資料

#函式可用於程式的包裝=>同樣的邏輯可以重複利用
def sum_1(a,b): #計算a加到b的總和
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    print(sum)

sum_1(1,10)
sum_1(1,20)
sum_1(5,10)