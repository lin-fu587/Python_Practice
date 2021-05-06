#主程式=>封包設計使用(要有__init__.py程式，資料夾才會被當成封包)
import geometry.point   #封包中的模組
result=geometry.point.distance(3,4) #使用封包中的模組中的函式
print("距離",result)

import geometry.line as line    #將封包中的模組改用別名
result=line.slope(1,1,3,3)
print("斜率",result)