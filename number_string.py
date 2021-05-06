#數字運算
x=3+6
x=3*6
x=10/6   #小數除法=>除不盡會幫你除到小數
x=10//6  #整數除法=>最多只會除到整數(小數部分都不會有，無條件捨去)
x=2**3  #2的3次方
x=2**0.5    #2開2次方根
x=7%3   #取餘數
print(x)
x=2+3
print(x)
x=x+1   #x+=1 將變數中資料+1
print(x)
#字串運算
s="hello\"c"   #字串可用雙引號或單引號(\有斜線是跳脫可以顯示雙引號，為了與外邊雙引號區隔)
s="hello"+"world"   #字串串接(中間+號換空白也是字串串接)
s="hello\nworld"    #多行
s="""hello  


world"""    #3個雙引號可以直接多行
s="hello"*3 #字串重複3遍
s="hello"*3+"world" #結果:hellohellohelloworld
s="hello"
print(s[0])
print(s[1:4])   #結果:ell=>可以直接印出子字串(編號從1到3，包含開頭不包含結尾)
print(s[1:])    #結果:ello
print(s[:4])    #結果:hell
