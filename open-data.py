#網路連線
# import urllib.request as request    #urllib是封包，request是封包中的模組(c語言中的.h檔)
# src="http://www.ntu.edu.tw/"
# with request.urlopen(src) as response:  #像是使用檔案的語法(with as)，as會回傳一個可操作的物件(就像c語言的檔案指標變數)
#                     #urlopen函式中放網址字串
#     data=response.read().decode("utf-8")    #取得台灣大學網站的原始碼(HTML,CSS,JS=>網頁的前端)
#                         #在後面加的decode是用來表示出中文的
# print(data1)
# print(data)

#串接，擷取公開資料=>有API網址可以直接網路連線獲取資料喔
import json
import urllib.request as request
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response)    #利用json模組處理json資料
#print(data)

#將公司名稱列表出來
clist=data["result"]["results"] #找出列表資料
#print(clist)
for i in clist: #clist將列表中的每一個字典資料丟入i=>i將會從第1個字典丟到第999個字典
    print(i["公司名稱"]+"\n")
#將處理的資料丟入新開的檔案中
with open("data_2.txt",mode="w",encoding="utf-8") as data_2:
    for i in clist: #clist將列表中的每一個字典資料丟入i=>i將會從第1個字典丟到第999個字典
        data_2.write(i["公司名稱"]+"\n")    #"字"+"字"=>字串串接
