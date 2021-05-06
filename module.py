#載入內建sys模組
import sys
print(sys.platform)
print(sys.maxsize)

#調整搜尋模組的路徑
import sys
sys.path.append("modules") #新增"modules"路徑，"modules"=>相對路徑=>相對於當前資料夾下的路徑

print(sys.path) #印出模組的搜尋路徑=>模組要放進指定中的資料夾=>找模組會從列表中的路徑找

#新增別名，使用模組的別名=>s
import sys as s
print(s.platform)
print(s.maxsize)

#建立geometry模組，載入使用(自訂模組)
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)
