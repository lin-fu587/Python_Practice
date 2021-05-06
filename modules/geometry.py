#在此模組中定義幾何運算功能

#計算兩點間距離
def distance(x1,y1,x2,y2):  
    return ((x2-x1)**2+(y2-y1)**2)**0.5

#計算線段斜率
def slope(x1,x2,y1,y2): 
    return (y2-y1)/(x2-x1)
    