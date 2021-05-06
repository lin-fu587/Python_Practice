#random 隨機模組
import random
data=random.choice([1,4,5,8])   #隨機選取資料變數中的一個數
print(data)

data=random.sample([1,3,2,5,8,10],3)    #隨機選取資料變數中的指定個數=>回傳列表
print(data)

data=[1,5,8,20]
random.shuffle(data)    #將列表中的資料調換順序=>會引響變數中的順序
print(data)

data=random.random()    #random()這個函式為0~1(只有0到1)之間的隨機亂數
print(data)

data=random.uniform(1.2,2.8)    #這個函式為1.2~2.8(幾到幾可更改)的隨機亂數
print(data)

#常態分配變數=>將得到的資料集中在中央(得到的資料多數在85和115之間)
data=random.normalvariate(100,15)    #後面兩個參數要給平均數和標準差
print(data)

#statistics 統計模組
import statistics as stat
data=stat.mean([1,4,5,8])    #取平均數
print(data)

data=stat.median([1,2,3,4,5,8,100]) #取中位數=>不會受極端數值影響
print(data)

data=stat.stdev([1,2,3,4,5,8,10])  #取標準差=>代表資料的集中程度
print(data)