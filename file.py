#開檔案(有兩種)

#1.
# fp1=open("d:\\PYTHON PRACTICE\\data.txt",mode="w",encoding="utf-8")  #開啟
# fp1.write("測試中文\n好棒棒") #操作=>如果是中文必須指定編碼
# fp1.close() #關閉

#2.
# with open("data.txt",mode="w",encoding="utf-8") as file:    #用with as會直接幫你釋放檔案不用寫close
#     file.write("5\n3")

#讀檔案
# with open("data.txt",mode="r",encoding="utf-8") as fp1:
#     data=fp1.read()
# print(data)

#讀檔案=>一行一行讀
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as fp1:
#     for i in fp1:   #一行一行讀
#         i=int(i)
#         sum=sum+i
# print(sum)

#使用JSON 格式讀取，放入data變數裡面
import json
with open("config.json",mode="r") as file:
    data=json.load(file)    #json檔案中的資料是字典
print(data)
print("name",data["name"]) #=>"字典型態"
print("version",data["version"])

data["name"]="new name" #修改變數中的資料
print(data)

#把新資料複寫回檔案中
with open("config.json",mode="w") as file:
    data=json.dump(data,file)   #將字典變數(資料)寫回json檔案
