import random
from matplotlib import pyplot as plt
def random_send_money(pop_num:int=100,times:int=10000,base_money:int=100):
    arr=[base_money for _ in range(pop_num)]
    for _ in range(times):
        for i in range(pop_num):
            id=random.randint(0,pop_num-1)
            # print(id)
            arr[i]=arr[i]-1
            arr[id]=arr[id]+1
    plt.plot(arr)
    plt.show()

if __name__=="__main__":
    # random_send_money()
    x=[1, 2, 3, 4]
    #y坐标轴上点的数值
    y=[1, 4, 9, 16]
    #第2步：使用plot绘制线条第1个参数是x的坐标值，第2个参数是y的坐标值
    plt.plot(x,y)
    #第3步：显示图形
    plt.show()
