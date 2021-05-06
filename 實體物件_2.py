#實體方法(函式)
#point實體物件的設計:   平面座標的點
class point:
    def __init__(self,x,y):
        self.x=x    #建立兩個實體屬性x,y
        self.y=y    
    #定義實體方法(函式)=>對齊初始化函式
    def show(self):
        print(self.x,self.y)
    def distance(self,targetx,targety):
        return ((targetx-self.x)**2+(targety-self.y)**2)**0.5


p=point(3,4)    #呼叫初始化函式，建立實體物件放入變數p中
p.show()    #呼叫實體方法(函式)=>實體實體物件.實體方法(函式)名稱(參數)
data=p.distance(0,0)    #計算座標(3,4)和座標(0,0)之間的距離
print(data)

#file 實體物件的設計:包裝檔案讀取的程式
class file:
    def __init__(self,name):
        self.name=name
        self.file=None  #尚未開啟檔案,初期式None=>file是檔案物件(檔案變數，同時也是實體屬性)
    def open(self): #實體方法(函式)
        self.file=open(self.name,mode="r",encoding="utf-8")   #PYTHON內建開啟檔案的函式=>回傳檔案物件(變數)放到實體屬性(變數)中
    def read(self):
        return self.file.read()

#讀取第一個檔案
f1=file("data_3.txt")   #建立實體物件(會呼叫初始化函式)並給予實體屬性
f1.open()   #呼叫實體方法
data=f1.read()  #呼叫實體方法
print(data)

#讀取第二個檔案
f2=file("data_4.txt")
f2.open()
data=f2.read()
print(data)