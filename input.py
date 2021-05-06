
from input import*
##############3
#n=int(input('請輸入數字'))
if __name__ == "__main__":
    b=int(input("請輸入一個數值:"))
    a=sum(b)
    print(a)

def sum(z):
    temp=0
    for i in range(1,z+1):
        temp=temp+i
    return temp
    
