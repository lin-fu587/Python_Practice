#if判斷式
#1.if
if True:
    print("True 執行")
if False:
    print("執行")

#2.if-else
if False:
    print("True 執行")
else:
    print("False 執行")

#3.if-elif-else

x=input("請輸入數字:")  #取得字串形式的使用者輸入(input("請輸入數字:"))，將字串輸入丟入x
x=int(x)    #將字串型態轉成數字型態
if x>200:
    print("大於200")
elif x>100:
    print("大於100，小於等於200")
else:
    print("小於等於100")

#4.四則運算
n1=int(input("請輸入數字:"))
n2=int(input("請輸入數字:"))
op=input("請輸入想要做的運算 ex.+,-,*,/: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")
