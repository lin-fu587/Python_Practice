#有序可變動列表List
grades=[12,60,15,70,90]

print(grades[0])

grades[0]=55    #把55放到列表中第一個位置
print(grades)

print(grades[1:4])

grades[1:4]=[]  #連續刪除列表中從編號1到編號3的資料
print(grades)

grades=grades+[12,33]   #列表串接
print(grades)

print(len(grades))  #len(列表資料)=>取得列表長度

data=[[3,4,5],[6,7,8]]  #巢狀列表
print(data[1][2])
data[0][0:2]=[5,5,5]
print(data)

#有序不可變動列表Tuple(除了資料不能再作更動以外，其餘操作都跟List一樣)
x=(3,4,5)
print(x[0:2])
x[0]=5  #錯誤:Tuple的資料不可以變動
print(x)