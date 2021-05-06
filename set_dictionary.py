#集合set=>大括弧(沒有順序)
s1={3,4,5}
print(3 in s1)  #測試是否有在集合中
print(10 not in s1) #測試是否不在集合中

s2={4,5,6,7}
s3=s1&s2    #交集:取兩個集合中相同的資料
print(s3)

s3=s1|s2    #聯集；取兩個資料中所有的資料，但不重複取
print(s3)

s3=s1-s2    #差集:從s1中減去和s2重複的部分
print(s3)

s3=s1^s2    #反交集；取兩個集合沒有重疊的部分，ex.{4,5}是重疊部分，取不重疊的{3,6,7}
print(s3)

s=set("hello")  #set(字串)=>會將字串拆成一個一個字元的集合，不會有重複字元
print(s)
print("h" in s)
print("a" in s)

#字典dictionary=>key對應value pairs(可以變更內部的值)
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"]) #用key找出值

dic["apple"]="西瓜"
print(dic["apple"])
print(dic)
print("apple" in dic)   #判斷key是否有在字典中(只有key)
print("test" not in dic)

del dic["apple"]    #刪除字典中的鍵值對
print(dic)

dic={x:x*2 for x in [3,4,5]}    #以列表資料產生字典
print(dic)