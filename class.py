#定義類別=>跟c語言的structure很像，一樣是封裝一般型態變數和函式在裡面
#         ，不過class可以直接用建立好的型態名稱使用內部屬性
#         ，structure要先建立此新型態變數，用變數名稱使用內部屬性

#定義類別IO，有兩個屬性(一個變數，一個函式，放在類別裡都稱類別的屬性)
class IO:
    supportedSrcs=["consoles","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from",src)

#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")