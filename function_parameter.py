#預設資料
def power(base,exp=0):  #預設次方exp=0
    print(base**exp)

power(3,2)  
power(4)    #假如呼叫函式沒給參數值將會使用預設值(前提是有設預設值，沒設定預設值也沒給參數將會變成error)    

#名稱對應
def divide(n1,n2):
    print(n1/n2)

divide(2,4)
divide(n2=2,n1=4)   #在呼叫函式給參數時，也可以直接寫(變數=數值)，函示將會照著內部變數對應給值

#無限/不定長度參數=>在參數前加上*  (在呼叫函式給定參數後將會把參數轉換成tuple變數)
def avg(*numbers):
    sum=0    
    for i in numbers:
        sum=sum+i
    print(sum/len(numbers))

avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)    

