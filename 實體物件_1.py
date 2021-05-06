#實體物件，實體屬性(變數)
#point 實體物件的設計: 平面座標上的點

class point:    #=>定義類別是為了產生實體物件
    def __init__(self,x,y):
        self.x=x    #self.x的x是實體屬性，外邊的x是參數
        self.y=y    #self.y的y是實體屬性，外邊的y是參數

#建立第一個實體物件
p=point(3,4)   #point()產生實體物件放到變數裡
print(p.x,p.y)

#建立第二個實體物件
p1=point(5,6)
print(p1.x,p1.y)

#fullname 實體物件的設計:分開紀錄姓,名資料的全名
class fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=fullname("Y.F","LIN")    #fullname()建立實體物件放入name1變數中
print(name1.first,name1.last)

name2=fullname("T.Y","LIN")
print(name2.first,name2.last)
